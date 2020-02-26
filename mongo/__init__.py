from flask import Flask
from .extensions import mongo_client
from .main import main

def create_app(config_object='mongo.settings'):
    app = Flask(__name__)

    app.config.from_object(config_object)

    app.register_blueprint(main)

    return app