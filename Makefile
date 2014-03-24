# pydemi
# https://github.com/chrisenytc/pydemi
#
# Copyright (c) 2014 Christopher EnyTC
# Licensed under the MIT license.


install:
	virtualenv venv
	source venv/bin/activate
	sudo pip install -r requirements.txt

start:
	@PY_ENV=production python runserver.py

test:
	@PY_ENV=test python test/test_pydemi.py

.PHONY: install test