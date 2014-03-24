# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
from mongoengine import *


class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    roles = ListField(default=['user'])
    token = StringField(required=True, unique=True)
