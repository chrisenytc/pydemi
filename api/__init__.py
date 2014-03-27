# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# version
__version__ = '0.2.0'

# Dependencies
import os
from api.config.development import Development
from api.config.production import Production
from api.config.test import Test
from api.errors.invalid_request import InvalidRequest
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


@app.errorhandler(Exception)
def handle_all_errors(error):
    try:
        response = JSON(error=error.to_dict().get('__all__'))
    except Exception:
        response = JSON(error=str(error))

    response.status_code = 500
    return response


@app.errorhandler(InvalidRequest)
def handle_invalid_request(error):
    response = JSON(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(500)
def internal_server_error(error):
    response = JSON(error=str(app.config['ERRORS']['500']))
    response.status_code = 500
    return response


@app.errorhandler(503)
def service_unavailable_error(error):
    response = JSON(error=str(app.config['ERRORS']['503']))
    response.status_code = 503
    return response


@app.errorhandler(400)
def bad_request(error):
    response = JSON(error=str(app.config['ERRORS']['400']))
    response.status_code = 400
    return response


@app.errorhandler(401)
def unauthorized(error):
    response = JSON(error=str(app.config['ERRORS']['401']))
    response.status_code = 401
    return response


@app.errorhandler(404)
def page_not_found(error):
    response = JSON(error=str(app.config['ERRORS']['404']))
    response.status_code = 404
    return response


# Import
from api.models import *
from api.controllers import *
