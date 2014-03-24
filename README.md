#PyDemi [![Build Status](https://secure.travis-ci.org/chrisenytc/pydemi.png?branch=master)](http://travis-ci.org/chrisenytc/pydemi) [![GH version](https://badge-me.herokuapp.com/api/gh/chrisenytc/pydemi.png)](http://badges.enytc.com/for/gh/chrisenytc/pydemi) [![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/chrisenytc/pydemi/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

> A wonderful API stack for python

## Getting Started

1º Clone pydemi repo

```bash
git clone https://github.com/chrisenytc/pydemi.git
```

2º Enter in pydemi directory
```bash
cd pydemi
```

3º Install dependencies

if you no have virtualenv installed. Install it.

```bash
sudo apt-get install python-virtualenv
```

```bash
virtualenv venv
```

```bash
source venv/bin/activate
```

```bash
make install
```

4º Configure the settings in `api/config`

5º Run pydemi

```bash
make start
```

Test your pydemi app

```bash
make test
```

## Controllers

How to use controllers

Conventions:

- All models can be found at: `from api.models.modelname import ModelName`. e.g: `from api.models.user import User`
- All configurations can be found at: `from api import app`. e.g: `app.config['API']`

Example:

```python
# -*- coding: utf-8 -*-

# Dependencies
from api import app
from flask import jsonify as JSON


@app.route('/')
def index():
    return JSON(welcome='Welcome to PyDemi API')

```

##### Enable CORS

To enable cors in pyDemi you have to use the decorator: `@cors`

Example:

```python
# -*- coding: utf-8 -*-

# Dependencies
from api import app
from flask import jsonify as JSON
from cors import cors


@app.route('/')
@cors(origin='*', methods=['GET'])
def index():
    return JSON(welcome='Welcome to PyDemi API')

```

##### Require Authentication

To protect your routes in pyDemi you have to use the decorator: `@require_auth`

Example:

```python
# -*- coding: utf-8 -*-

# Dependencies
from api import app
from flask import jsonify as JSON
from auth import require_auth


@app.route('/')
@require_auth(roles='*')
def index():
    return JSON(welcome='Welcome to PyDemi API')

```

##### Access user data

Example:

```python
# -*- coding: utf-8 -*-

# Dependencies
from api import app
from flask import jsonify as JSON
from flask import request
from auth import require_auth


@app.route('/')
@require_auth(roles='*')
def index():
    return JSON(user=request.user) # Returns a dict with the user data

```

## Models

How to use models

Example:

`api/models/task.py`

```python
# -*- coding: utf-8 -*-

# Dependencies
from mongoengine import *


class Task(Document):
    slug = StringField(require=True, unique=True)
    description = StringField(default='')
    closed = BooleanField(default=False)

```

##### Using the model

Example:

`api/controllers/tasks.py`

```python
# -*- coding: utf-8 -*-

# Dependencies
from api import app
from flask import request
from flask import jsonify as JSON
from api.models.task import Task


@app.route('/tasks', methods=['POST'])
def create():
    # Create new task
    new_task = Task()
    new_task.slug = request.form['slug']
    new_task.description = request.form['description']
    new_task.save()
    return JSON(message='Task created successfully')

```

For more information about mongoengine, see documentation [here](http://docs.mongoengine.org/)

## Contributing

See the [CONTRIBUTING Guidelines](CONTRIBUTING.md)

## Support
If you have any problem or suggestion please open an issue [here](https://github.com/chrisenytc/pydemi/issues).

## License

Copyright (c) 2014 Christopher EnyTC

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.