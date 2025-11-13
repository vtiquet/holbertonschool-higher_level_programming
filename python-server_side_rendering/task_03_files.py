from flask import Flask, render_template, request
import json
import csv
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_folder)


def load_products_json(file_path):
    """Loads product data from a JSON file."""
    try:
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError, Exception) as e:
        print(f"Error loading JSON data: {e}", file=os.sys.stderr)
        return None


def load_products_csv(file_path):
    """Loads product data from a CSV file."""
    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
            for row in data:
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except (ValueError, KeyError):
                    continue
        return data
    except (FileNotFoundError, Exception) as e:
        print(f"Error loading CSV data: {e}", file=os.sys.stderr)
        return None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    file_path = os.path.join(base_dir, 'items.json')
    try:
        with open(file_path, 'r') as file:
            items_data = json.load(file).get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_data = []

    return render_template('items.html', items=items_data)


@app.route('/products')
def products():
    """Renders products from 'json' or 'csv' source,
    with optional ID filtering."""
    source = request.args.get('source')
    product_id_str = request.args.get('id')

    products_data = None

    if source == 'json':
        file_path = os.path.join(base_dir, 'products.json')
        products_data = load_products_json(file_path)

    elif source == 'csv':
        file_path = os.path.join(base_dir, 'products.csv')
        products_data = load_products_csv(file_path)

    else:
        return render_template('product_display.html', error='Wrong source')

    if products_data is None:
        return render_template(
            'product_display.html',
            error=f'Could not load data from {source} file'
        )

    if product_id_str:
        try:
            products_data = [
                p for p in products_data
                if str(p.get('id')) == product_id_str
            ]
        except Exception:
            products_data = []

        if not products_data:
            return render_template(
                'product_display.html',
                error='Product not found'
            )

        return render_template(
            'product_display.html',
            product=products_data[0],
            source=source
        )

    return render_template(
        'product_display.html',
        products=products_data,
        source=source
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
