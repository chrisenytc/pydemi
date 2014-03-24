# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# version
__version__ = '0.1.0'

# Dependencies
import os
from api.config.development import Development
from api.config.production import Production
from api.config.test import Test
from flask import Flask
from flask import jsonify as JSON
from mongoengine import connect

# Start Flesk
app = Flask('pydemi')

# Configs
env = os.environ.get('PY_ENV', 'development')

if env == 'development':
    app.config.from_object(Development)
elif env == 'production':
    app.config.from_object(Production)
elif env == 'test':
    app.config.from_object(Test)
else:
    print 'Environment not found'

# Debug mode
app.debug = app.config['API']['debug']

# Connect on mongodb
connect('pydemi', host=os.environ.get('MONGOLAB_URI')
        or os.environ.get('MONGOHQ_URL') or app.config['DATABASE']['uri'])


@app.errorhandler(500)
def page_not_found(error):
    return JSON(error=str(app.config['ERRORS']['500']))


@app.errorhandler(401)
def unauthorized(error):
    return JSON(error=str(app.config['ERRORS']['401']))


@app.errorhandler(404)
def internal_server_error(error):
    return JSON(error=str(app.config['ERRORS']['404']))

# Import
from api.models import *
from api.controllers import *
