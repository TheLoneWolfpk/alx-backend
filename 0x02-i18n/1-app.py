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


app.config.from_object('1-app.Config')


@app.route('/')
def default():
    '''Return 1-index.html template'''
    return render_template('1-index.html')
