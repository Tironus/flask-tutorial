from flask import Blueprint

from .extensions import mongo_client
from .db import create_doc, display_doc, display_id

main = Blueprint('main', __name__)

@main.route('/')
def index():
    mdb = mongo_client.OSRIC
    char1 = create_doc(mdb, 'Tiro', 10, 4, 5)
    found_chars = display_doc(mdb, 'Tiro')
    #found_chars = display_id(mdb, "5e56fc630000b90542314c86")
    return str(found_chars)