# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""


class Test():
    API = {
        'name': 'PyDemi - Test',
        'description': 'A wonderful API framework for python',
        'version': 'v1',
        'debug': True,
        'documentation_url': ''
    }
    AUTH = {
        'enabled': False
    }
    DATABASE = {
        'uri': 'mongodb://localhost/pydemidb-test'
    }
    ERRORS = {
        '500': 'Internal Server Error',
        '401': 'Bad Authentication. You do not have permission to access the API',
        '404': 'Not Found'
    }
