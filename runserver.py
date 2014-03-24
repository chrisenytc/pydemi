#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""
ProjectName: pydemi
Repo: https://github.com/chrisenytc/pydemi
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import os
from api import app

# Start pyDemi
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 22792))
    app.run('0.0.0.0', port=port)
