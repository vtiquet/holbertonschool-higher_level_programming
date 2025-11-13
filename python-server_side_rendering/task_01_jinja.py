from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Renders the home page using the index.html template."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Renders the about page using the about.html template."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Renders the contact page using the contact.html template."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
