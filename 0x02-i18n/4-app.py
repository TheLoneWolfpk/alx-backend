#!/usr/bin/env python3
'''
instantiating Babel object in flask application
'''


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''
    flask application config class
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    '''Determine the best match with supported languages'''
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    locale = request.accept_languages.best_match(Config.LANGUAGES)
    return locale


app.config.from_object('4-app.Config')


@app.route('/')
def default():
    '''Return 4-index.html template'''
    return render_template('4-index.html')
