#!/usr/bin/env python3
'''
instantiating Babel object in flask application
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    '''
    flask application config class
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    '''Determine the best match with supported languages'''
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.get('user') and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    '''Returns a user dictionary or None, if the user doesn't exist'''
    user_id = request.args.get('login_as')
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None

@app.before_request
def before_request():
    '''Handles request before making the request to the API'''
    user = get_user()
    if user:
        g.user = user

@app.route('/')
def default():
    '''Return 5-index.html template'''
    current_time = datetime.now().strftime("%b %d, %Y, %I:%M:%S %p")
    message = gettext("The current time is %(current_time)s.", current_time=current_time)
    return render_template('5-index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)

