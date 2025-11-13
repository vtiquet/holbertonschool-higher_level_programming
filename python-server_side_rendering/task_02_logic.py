from flask import Flask, render_template
import json
import os

app = Flask(__name__)


def load_items_data():
    """Reads items from the items.json file."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'items.json')

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # The structure is {"items": [...]}, so we extract the list
            return data.get('items', [])
    except FileNotFoundError:
        print("Error: items.json not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Could not decode items.json.")
        return []


@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Reads items.json and renders them using items.html."""
    items_list = load_items_data()
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
