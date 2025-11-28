<div align="center"><img src="https://github.com/vtiquet/holbertonschool-resources/blob/main/image/Holberton-Logo.svg" width=40% height=40%/></div>

# Resources

## Table of Contents :

  - [0. Color Me](#subparagraph0)
  - [1. Click and turn red](#subparagraph1)
  - [2. Add `.red` class](#subparagraph2)
  - [3. Toggle classes](#subparagraph3)
  - [4. List of elements](#subparagraph4)
  - [5. Change the text](#subparagraph5)
  - [6. Star wars character](#subparagraph6)
  - [7. Star Wars movies](#subparagraph7)
  - [8. Say Hello!](#subparagraph8)
  - [9. List, add, remove](#subparagraph9)
  - [10. Say hello to everybody!](#subparagraph10)

## Resources
### Read or watch:
* [What is JavaScript?](/rltoken/BRGugPVlpApb5CMpWDZZyw)
* [Introduction to the DOM](/rltoken/_IqetddeDl77jcNAfU8lSQ)
* [Document Interface](/rltoken/VBwvMfwoElIcvVa-Rc9LJg)
* [Element Class](/rltoken/3f2toV3UxRn01mxEV3o9Xg)
* [Locating DOM elements using selectors](/rltoken/X2TAX96ZFGmNHfVXEK4iuQ)
* [CSS Selectors](/rltoken/o7C085ffGbWw-5LySsOWww)
* [CSS Diner](/rltoken/GunCAsRgUiuvrDkp07w6jw)
* [DOM Scripting](/rltoken/IyYBDmVhUL-DAbLlMkeJWQ)
* [Network Requests](/rltoken/sqJbOOIcK_OQGQGW6VXhKw)
* [What went wrong? Troubleshooting JavaScript](/rltoken/vudThPsuSBng13jFlPyI0Q)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
* How to select HTML elements in JavaScript
* What are differences between ID, class and tag name selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a request with XmlHTTPRequest
* How to make a request with Fetch API
* How to listen/bind to DOM events
* How to listen/bind to user events

## Requirements
### General
* Allowed editors: All of them.
* All your files will be interpreted on Chrome browser (version 57.0 or later)
* All your files should end with a new line
* A mandatoryREADME.mdfile with meaningful information about the content, should be placed at the root folder of the project.
* Your code should besemistandardcompliant
* You are not allowed to use var
* HTML should not reload for each action: DOM manipulation, update values, fetch data…

## Task
### 0. Color Me <a name='subparagraph0'></a>

Write a JavaScript script that updates the text color of the <code>header</code> element to red (<code>#FF0000</code>):

* You must use <code>document.querySelector</code> to select the HTML tag

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 1. Click and turn red <a name='subparagraph1'></a>

Write a JavaScript script that updates the text color of the <code>header</code> element to red (<code>#FF0000</code>) when the user clicks on the tag with id <code>red_header</code>:

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 2. Add `.red` class <a name='subparagraph2'></a>

Write a JavaScript script that adds the class <code>red</code> to the <code>header</code> element when the user clicks on the tag with id <code>red_header</code>

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 3. Toggle classes <a name='subparagraph3'></a>

Write a JavaScript script that toggles the class of the <code>header</code> element when the user clicks on the tag id <code>toggle_header</code>:

The <code>header</code> element must always have one class: <code>red</code> or <code>green</code>, never both in the same time and never empty.
If the current class is <code>red</code>, when the user click on id <code>toggle_header</code> element, the class must be updated to <code>green</code> ; and the reverse.

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 4. List of elements <a name='subparagraph4'></a>

Write a JavaScript script that adds a <code>li</code> element to a list when the user clicks on the element with id <code>add_item</code>:

The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code>
The new element must be added to the <code>ul</code> element with class <code>my_list</code>

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 5. Change the text <a name='subparagraph5'></a>

Write a JavaScript script that updates the text of the <code>header</code> element to <code>New Header!!!</code> when the user clicks on the element with id <code>update_header</code>

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 6. Star wars character <a name='subparagraph6'></a>

Write a JavaScript script that fetches the character <code>name</code> from this URL: <code>https://swapi-api.hbtn.io/api/people/5/?format=json</code>

* The name must be displayed in the HTML tag with id <code>character</code>.
* You must use the <a href="/rltoken/mov5LF24GCfD957vJ0i7dg" target="_blank" title="Fetch API">Fetch API</a>.
* You probably should read something about <a href="/rltoken/sRgTVb2pzsne9C5-2xIJvQ" target="_blank" title="usign Promises">usign Promises</a> later.

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 7. Star Wars movies <a name='subparagraph7'></a>

Write a JavaScript script that fetches and lists the <code>title</code> for all movies by using this URL: <code>https://swapi-api.hbtn.io/api/films/?format=json</code>

* All movie titles must be list in the HTML <code>ul</code> element with id <code>list_movies</code>
* You must use the Fetch API.

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 8. Say Hello! <a name='subparagraph8'></a>

Write a JavaScript script that fetches from <code>https://hellosalut.stefanbohacek.com/?lang=fr</code> and displays the value of <code>hello</code> from that fetch in the HTML element with id <code>hello</code>.

* The translation of “hello” must be displayed in the HTML element with id <code>hello</code>
* Your script must work when it is imported from the <code>&lt;head&gt;</code> tag

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="8-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 9. List, add, remove <a name='subparagraph9'></a>

Write a JavaScript script that adds, removes and clears <code>li</code> elements from a list when the user clicks:

* The new element must be: <code>&lt;li&gt;Item&lt;/li&gt;</code>
* The new element must be added to the element with id <code>my_list</code>
* When the user clicks on the element with id <code>add_item</code>: a new element is added to the list
* When the user clicks on the element with id <code>remove_item</code>: the last element is removed from the list
* When the user clicks on the element with id <code>clear_list</code>: all elements of the list are removed
You script must work when it imported from the <code>head</code> tag
Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---

### 10. Say hello to everybody! <a name='subparagraph10'></a>

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

* You should use this API service: <code>https://hellosalut.stefanbohacek.com/</code>
* The language code will be the value selected in the combo box with id <code>language_code</code> (es, fr, en etc.)
* The translation must be fetched when the user clicks on element with id <code>btn_translate</code>
* The translation of “Hello” must be displayed in the HTML tag with id <code>hello</code>
* You script must work when imported from the <code>&lt;head&gt;</code> tag

Please test with this HTML file in your browser:

```
javiercito@ubuntu:~/javascript-dom_manipulation$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <label for="language_code">Language code:</label>
    <select name="language" id="language_code">
        <option value="">--Please choose an option--</option>
        <option value="en">English</option>
        <option value="es">Spanish</option>
        <option value="fr">French</option>
    </select>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2022
    </footer>
  </body>
</html>
javiercito@ubuntu:~/javascript-dom_manipulation$
```

---


## Authors
vtiquet - [GitHub Profile](https://github.com/vtiquet)
