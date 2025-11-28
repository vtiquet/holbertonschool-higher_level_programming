<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Titre du Projet (à remplacer)

## Table of Contents :

  - [0. Creating a Simple Templating Program](#subparagraph0)
  - [1. Creating a Basic HTML Template in Flask](#subparagraph1)
  - [2. Creating a Dynamic Template with Loops and Conditions in Flask](#subparagraph2)
  - [3. Displaying Data from JSON or CSV Files in Flask](#subparagraph3)
  - [4. Extending Dynamic Data Display to Include SQLite in Flask](#subparagraph4)

## Task
### 0. Creating a Simple Templating Program <a name='subparagraph0'></a>

In this task, you will create a Python function that generates personalized invitation files from a template with placeholders and a list of objects. Each output file should be named sequentially, starting from 1. You will also implement specific error handling for various edge cases.

* Understand how to use string templating in Python.
* Implement file operations for reading templates and writing output files.
* Handle various edge cases and errors gracefully.

* <p><strong>Check Input Types:</strong></p>

  * Verify that <code>template</code> is a string and <code>attendees</code> is a list of dictionaries.
  * If <code>template</code> is not a string or <code>attendees</code> is not a list of dictionaries, log an error message and terminate the function.
* <p><strong>Handle Empty Inputs:</strong></p>

  * Check if the template is empty and log an error message if it is.
  * Check if the attendees list is empty and log an error message if it is.
* <p><strong>Process Each Attendee:</strong></p>

  * Iterate over the list of attendees and replace the placeholders in the template with the corresponding values from each attendee’s dictionary.
  * If a value is missing, replace it with “N/A”.
* <p><strong>Generate Output Files:</strong></p>

  * Write the processed template to output files named <code>output_X.txt</code>, where <code>X</code> is the index of the attendee starting from 1.

```
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
```

```
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]
```

```
# Main file content
from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)
```

* Use Python’s string <code>replace</code> method to substitute placeholders with actual values.
* Use <code>os.path.exists</code> to check if a file already exists before writing.
* Use <code>try</code> and <code>except</code> blocks to handle potential errors gracefully.

* <strong>Python String Methods</strong>: <a href="/rltoken/W6bJdwDnBI2Ei0brfUqCJw" target="_blank" title="Python Official Documentation">Python Official Documentation</a>
* <strong>File Handling in Python</strong>: <a href="/rltoken/1T4vhH1weF8SheeeZYeeLA" target="_blank" title="Python Official Documentation">Python Official Documentation</a>

---

### 1. Creating a Basic HTML Template in Flask <a name='subparagraph1'></a>

In this task, you will build a basic Flask application that serves a web page using a Jinja template. You will create a simple HTML template that includes various elements like headings, paragraphs, and lists, and learn how to render it as a web page using Flask. Additionally, you will learn to create reusable templates for headers and footers to promote code reusability and consistency across multiple pages.

* Set up a Flask environment and create a basic Flask application.
* Design HTML templates using Jinja for dynamic content rendering.
* Implement reusable components in templates to maintain consistent layout across pages.

```
from flask import Flask, render_template

   app = Flask(__name__)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == '__main__':
       app.run(debug=True, port=5000)
```

Content for <code>index.html</code>:

```
<!doctype html>
   <html lang="en">
   <head>
       <title>My Flask App</title>
   </head>
   <body>
       <h1>Welcome to My Flask App</h1>
       <p>This is a simple Flask application.</p>
       <ul>
           <li>Flask</li>
           <li>HTML</li>
           <li>Templates</li>
       </ul>
   </body>
   </html>
```

Content for <code>header.html</code>:

```
<header>
       <h1>My Flask App</h1>
   </header>
```

Content for <code>footer.html</code>:
   <code>html
   &lt;footer&gt;
       &lt;p&gt;&amp;copy; 2024 My Flask App&lt;/p&gt;
   &lt;/footer&gt;
</code>

```
- Add specific tags for each page:
     - In `about.html`, include an   `<h1>` tag with the text "About Us" and a paragraph (`<p> `) with content describing the page.
     - In `contact.html`, include an  `<h1> `  tag with the text "Contact Us" and a paragraph (`<p>`) with content for the contact page.
```

```
@app.route('/about')
   def about():
       return render_template('about.html')

   @app.route('/contact')
   def contact():
       return render_template('contact.html')
```

* Ensure your Flask application runs on port 5000.
* Use the <code>render_template</code> function from Flask to render HTML templates.
* Utilize Jinja’s <code>{% include %}</code> statement to include reusable components like headers and footers.

* <strong>Flask Quickstart:</strong> <a href="/rltoken/xLnef6coA0Lgt71gTcnS5Q" target="_blank" title="Flask Quickstart">Flask Quickstart</a>
* <strong>HTML Basics:</strong> <a href="/rltoken/3s9aM9mrDsmWx6I-V7zokw" target="_blank" title="HTML Tutorial on W3Schools">HTML Tutorial on W3Schools</a>
* <strong>Flask Templating with Jinja:</strong> <a href="/rltoken/RWlt7-FqgostaP1MpAJnXg" target="_blank" title="Flask Templating">Flask Templating</a>
* <strong>Jinja Template Inheritance:</strong> <a href="/rltoken/oT7L0anPHrZ-Q42K1Lp8ig" target="_blank" title="Jinja Template Inheritance">Jinja Template Inheritance</a>

---

### 2. Creating a Dynamic Template with Loops and Conditions in Flask <a name='subparagraph2'></a>

In this task, you will enhance your Flask application by integrating dynamic content into your HTML templates using Jinja’s loop and conditional constructs. You will read a list of items from a JSON file and display them dynamically on a web page.

* Use Jinja’s loop and conditional constructs to dynamically render content in HTML templates.
* Read and parse JSON data in Python.
* Integrate dynamic content into your Flask application.

* Experiment with different lists, including an empty list, to see how your template responds.

```
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```

* Use Python’s <code>json</code> module to read data from the JSON file.
* Utilize Jinja’s <code>{% for %}</code> loop to iterate over the list of items in the template.
* Use the <code>{% if %}</code> statement to conditionally display the message when the list is empty.
* Define the new route <code>/items</code> in your Flask application and use the <code>render_template</code> function to pass the list of items to <code>items.html</code>.

* <strong>Jinja Template Designer Documentation:</strong> <a href="/rltoken/8JdOhBd-JaExBWwtyVJuew" target="_blank" title="Jinja Template Designer Documentation">Jinja Template Designer Documentation</a>
* <strong>Flask Templating with Jinja:</strong> <a href="/rltoken/RWlt7-FqgostaP1MpAJnXg" target="_blank" title="Flask Templating">Flask Templating</a>

After setting up the dynamic template and route, run your Flask application and navigate to the new route.  Verify that the list of items is correctly displayed on the page. Test with different lists, including an empty list, to ensure that the conditional statement works as expected.

---

### 3. Displaying Data from JSON or CSV Files in Flask <a name='subparagraph3'></a>

In this task, you will build a feature in your Flask application to read and display product data from two different data formats: JSON and CSV. You will create a single HTML template that can display data from either file type, depending on a query parameter provided in the URL. You will add functionality to your Flask application to filter product data based on an optional <code>id</code> query parameter. Additionally, you will handle edge cases such as invalid <code>source</code> parameter values or when the specified <code>id</code> is not found in the data.

* Read and parse data from JSON and CSV files.
* Use query parameters in Flask to determine data sources and filter criteria.
* Implement error handling for invalid inputs and missing data.
* Render dynamic data in HTML templates using Jinja.

* <p>Create a CSV file (<code>products.csv</code>) with similar data, using columns for <code>id</code>, <code>name</code>, <code>category</code>, and <code>price</code>.</p>
<pre><code> Example CSV content:
</code></pre>
<pre><code> id,name,category,price
 1,Laptop,Electronics,799.99
 2,Coffee Mug,Home Goods,15.99
</code></pre>

* Use Python’s <code>json</code> module to read data from the JSON file.
* Use Python’s <code>csv</code> module to read data from the CSV file.
* Utilize Flask’s <code>request.args</code> to get query parameters.
* Use Jinja’s templating features to conditionally display error messages and dynamic data.

* <strong>Reading JSON and CSV in Python:</strong>

  * JSON: <a href="/rltoken/lC6m9GFhAWqgqvmSlA3y5g" target="_blank" title="JSON in Python">JSON in Python</a>
  * CSV: <a href="/rltoken/FwAYKq-BrdtZlNodGDxsag" target="_blank" title="CSV File Reading and Writing">CSV File Reading and Writing</a>
* <strong>Flask Request Object:</strong> <a href="/rltoken/eQhOfyVFkLC5gR3NhPoVsA" target="_blank" title="Flask Request Object">Flask Request Object</a>
* <strong>Query Parameters in Flask:</strong> <a href="/rltoken/eQhOfyVFkLC5gR3NhPoVsA" target="_blank" title="Flask Request Object">Flask Request Object</a>
* <strong>Error Handling in Flask:</strong> <a href="/rltoken/c3p6vS48JY-Dvimfj3NPbw" target="_blank" title="Flask Error Handling">Flask Error Handling</a>

Test your application with various scenarios:

* Access URLs like <code>http://localhost:5000/products?source=json</code>, <code>http://localhost:5000/products?source=csv</code>, and <code>http://localhost:5000/products?source=xml</code> (invalid source).
* Test with and without the <code>id</code> parameter, and with both valid and invalid <code>id</code> values.
* Verify that the application correctly filters data, displays all products when no <code>id</code> is provided, and shows appropriate error messages for edge cases.

---

### 4. Extending Dynamic Data Display to Include SQLite in Flask <a name='subparagraph4'></a>

Building on the previous exercise, you will now add the functionality to fetch and display data from a SQLite database in your Flask application. The application should allow users to choose between JSON, CSV, and SQL (SQLite database) as data sources using the <code>source</code> query parameter.

* Set up and interact with a SQLite database in a Flask application.
* Extend existing functionality to handle multiple data sources.
* Implement error handling for database-related issues.

* <p><strong>Table Structure:</strong></p>

  * Create a <code>Products</code> table with columns: <code>id</code> (primary key), <code>name</code>, <code>price</code>, <code>category</code>.
* <p><strong>Example Data:</strong></p>

  * Insert the following data into the <code>Products</code> table:


    * <code>id</code>: 1, <code>name</code>: “Laptop”, <code>price</code>: 799.99, <code>category</code>: “Electronics”
    * <code>id</code>: 2, <code>name</code>: “Coffee Mug”, <code>price</code>: 15.99, <code>category</code>: “Home Goods”

Use the following script to create and populate the database:

```
import sqlite3

   def create_database():
       conn = sqlite3.connect('products.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Products (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               category TEXT NOT NULL,
               price REAL NOT NULL
           )
       ''')
       cursor.execute('''
           INSERT INTO Products (id, name, category, price)
           VALUES
           (1, 'Laptop', 'Electronics', 799.99),
           (2, 'Coffee Mug', 'Home Goods', 15.99)
       ''')
       conn.commit()
       conn.close()

   if __name__ == '__main__':
       create_database()
```

* Use Python’s <code>sqlite3</code> module to interact with the SQLite database.
* Define a function to read data from the SQLite database and convert it into a format suitable for rendering in the template.
* Use Flask’s <code>request.args</code> to get the <code>source</code> query parameter and determine the data source.

* <strong>Flask-SQLAlchemy:</strong> <a href="/rltoken/JBmvcrjCCGZGlWw1M-OI3A" target="_blank" title="Flask-SQLAlchemy">Flask-SQLAlchemy</a>
* <strong>SQLite in Python:</strong> <a href="/rltoken/wPc6yZmq5N00DfY5cfWRYQ" target="_blank" title="SQLite3 Module">SQLite3 Module</a>

Test your application with the URL query parameter set to <code>json</code>, <code>csv</code>, and <code>sql</code> to ensure that the correct data is displayed for each source. Verify that the application can handle and display errors appropriately for invalid sources or database issues.

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
