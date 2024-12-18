#!/usr/bin/env python3
"""task 1 creat a flask app"""


from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = FLASK(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """'/' route"""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(debug=True)
