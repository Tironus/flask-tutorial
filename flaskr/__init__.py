import os

from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

# connect to cloud mongodb
client = MongoClient('mongodb+srv://tony:tonydb1@cluster0-tony-fffjh.mongodb.net/test?retryWrites=true&w=majority')
db = client.admin

app.config['SECRET_KEY'] = 'dev'
app.config['DATABASE'] = db

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'