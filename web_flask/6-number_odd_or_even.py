#!/usr/bin/python3
""" Starts a Flask web application"""
from flask import *

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Prints a message when the route / is taken in the web application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints a message when the route /hbnb is taken in the web application"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Print c with a variable """
    return "C  wtv {}".format(text).replace("_", " ")


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """Print python with a variable and default value """
    return "Python {}".format(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Prints a message when the route / is taken in the web application"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def nTemplate(n):
    """Display h1 Number"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def evenOddTemplate(n):
    """Display h1 Number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """ Makes the app run when called from the command line"""
    app.run(host='0.0.0.0', port=5000)
