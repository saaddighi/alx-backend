#!/usr/bin/env python3
"""task 0 creat a flask app"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
     """'/' route"""
     return render_template('0-index.html',)


if __name__ == "__main__":
    app.run(debug=True)
