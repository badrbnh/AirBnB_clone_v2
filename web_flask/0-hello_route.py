#!/usr/bin/python3
""" Starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Prints a message when the route / is taken in the web application"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """ Makes the app run when called from the command line"""
    app.run(host='0.0.0.0', port=5000)
