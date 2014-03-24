# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""


class Production():
    API = {
        'name': 'PyDemi',
        'description': 'A wonderful API framework for python',
        'version': 'v1',
        'debug': False,
        'documentation_url': ''
    }
    AUTH = {
        'enabled': True
    }
    DATABASE = {
        'uri': 'mongodb://localhost/pydemidb'
    }
    ERRORS = {
        '500': 'Internal Server Error',
        '401': 'Bad Authentication. You do not have permission to access the API',
        '404': 'Not Found'
    }
