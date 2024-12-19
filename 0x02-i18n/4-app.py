#!/usr/bin/env python3
"""task 1 creat a flask app"""


from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import gettext as _


class Config:
    """config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """geting best language match"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """'/' route"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
