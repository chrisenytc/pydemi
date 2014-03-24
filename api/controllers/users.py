# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import uuid
from api import app
from hashlib import sha1
from flask import request
from flask import jsonify as JSON
from api.models.user import User
from cors import cors


@app.route('/signup', methods=['POST'])
@cors(origin='*', methods=['POST'])
def signup():
    # Create new user
    new_user = User()
    new_user.name = request.form['name']
    new_user.email = request.form['email']
    new_user.password = sha1(request.form['password']).hexdigest()
    new_user.token = str(uuid.uuid4())
    new_user.save()
    return JSON(message='User created successfully')


@app.route('/signin', methods=['POST'])
@cors(origin='*', methods=['POST'])
def signin():
    # Retorna a user data
    user_info = User.objects(email=request.form['email'], password=sha1(
        request.form['password']).hexdigest())
    if user_info.count():
        return JSON(token=user_info.get().token, roles=user_info.get().roles)
    else:
        return JSON(message='User not found')
