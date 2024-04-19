#!/usr/bin/python3
"""C is funn! and best"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return f'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return f'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
