import os

from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
from pprint import pprint

# create and configure the app
app = Flask(__name__, instance_relative_config=True)

# connect to cloud mongodb
client = MongoClient('mongodb+srv://tony:tonydb1@cluster0-tony-fffjh.mongodb.net/test?retryWrites=true&w=majority')
db = client.admin

app.config['SECRET_KEY'] = 'dev'
app.config['DATABASE'] = db

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# a simple page that says hello
@app.route('/mongo')
def mongo():
    serverStatusResult = db.command("serverStatus")
    return str(serverStatusResult['host'])