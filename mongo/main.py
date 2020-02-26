from flask import Blueprint

from .extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    status=db.command('serverStatus')
    return str(status)