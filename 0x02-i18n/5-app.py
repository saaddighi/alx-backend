
"""task 1 creat a flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from flask_babel import gettext as _


class Config:
    """config class """
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    user1 = request.args.get('login_as')
    if user1:
        return users.get(int(user1))
    return None

@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    """geting best language match"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """'/'route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
