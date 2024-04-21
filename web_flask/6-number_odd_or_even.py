#!/usr/bin/python3

""" Flask Web Application"""


from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function that returns Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function that returns hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Function that returns C followed by text variable """
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Function that returns Python followed by text variable """
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def numer_n(n):
    """ Function that displays n is a number only if n is an integer """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numer_template(n):
    """ Function that displays n is a number only if n is an integer """
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_odd_or_even(n):
    """Function that displays a HTML page only if n is an int"""
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
