# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
from api import app
from flask import jsonify as JSON
from cors import cors


@app.route('/')
@cors(origin='*', methods=['GET'])
def index():
    return JSON(welcome='Welcome to PyDemi API')
