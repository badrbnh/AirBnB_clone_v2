#!/usr/bin/python3
""" Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Prints a message when the route / is taken in the web application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints a message when the route /hbnb is taken in the web application"""
    return "HBNB"


if __name__ == '__main__':
    """ Makes the app run when called from the command line"""
    app.run(host='0.0.0.0', port=5000)
