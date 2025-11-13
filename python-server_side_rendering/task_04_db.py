from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_folder)
DATABASE = os.path.join(base_dir, 'products.db')


def get_db_connection():
    """Establishes and returns a SQLite database connection."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
    except sqlite3.Error as e:
        print(f"Database connection error: {e}", file=os.sys.stderr)
        return None
    return conn


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
    """
    Renders products from 'db', 'json', or 'csv' source,
    supporting optional ID filtering.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')

    products_data = None

    if source == 'db':
        conn = get_db_connection()
        if conn is None:
            return render_template(
                'product_display.html',
                error='Database connection failed'
            )

        cursor = conn.cursor()

        query = "SELECT id, name, category, price FROM Products"
        params = []

        if product_id_str:
            query += " WHERE id = ?"
            params.append(product_id_str)

        try:
            cursor.execute(query, tuple(params))
            products_data = [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"SQLite query error: {e}", file=os.sys.stderr)
            products_data = []
        finally:
            conn.close()

    elif source == 'json':
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
            error=f'Could not load data from {source} source'
        )

    if not products_data and product_id_str:
        return render_template(
            'product_display.html',
            error='Product not found'
        )

    return render_template(
        'product_display.html',
        products=products_data,
        source=source
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
