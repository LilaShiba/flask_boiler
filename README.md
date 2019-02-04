# Initialization

### Flask

```bash

pip3 install flask
pip install python-dotenv

```

### Create folder

``` bash
cd Desktop ; mkdir 01_flask ; cd 01_flask
```

### Create Root File Structure
![root_structure](app/static/images/root_img.png)

### Create App File Structure
![app_structure](app/static/images/app_tree.png)

### templates
Add a index.html with a short hello message

### .flaskenv
add the following lines
```python
FLASK_APP=main.py
FLASK_RUN_HOST=0.0.0.0
FLASK_RUN_PORT=8080
FLASK_DEBUG=1
FLASK_ENV=development
```

In the command line, write export and each line exactly as is.

### routes
```python
from flask import *
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
```

### Run Server
In the root directory, run

```bash
flask run
```

### Todo
- Add three new pages with routes

# Day Two
- Create form
- Display information

# Day Three
- API call

# Day Four
- Bootstrap & CSS
