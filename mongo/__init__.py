from flask import Flask
from .extensions import mongo

def mongo_app(config_object='mongo.settings'):
    app = Flask(__name__)

    app.config.from_object(config_object)

    mongo.init_app(app)

    return app