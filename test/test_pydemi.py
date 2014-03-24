# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import unittest


class TestPyDemi(unittest.TestCase):

    def setUp(self):
        self.test = "Welcome to PyDemi"

    def test_returns_a_hello_world(self):
        self.assertEqual(self.test, 'Welcome to PyDemi')

if __name__ == '__main__':
    unittest.main()
