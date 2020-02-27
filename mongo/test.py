from pymongo import MongoClient
import random
from bson.objectid import ObjectId

mongo_client = MongoClient('mongodb+srv://tony:tonydb1@cluster0-tony-fffjh.mongodb.net/test?retryWrites=true&w=majority')

mdb = mongo_client.OSRIC
col = mdb['dnd']
print(col.name)

query = {"_id" : ObjectId('5e571000551c9b30e54e123c')}
attr = random.randint(1, 100)
print(attr)
result = col.find_one(query)
print(result)
result = col.find_one_and_update(query, {'$set': {"attr1" : attr}})
result = col.find_one(query)
print(result)

# '5e571000551c9b30e54e123c'

# char1 = create_doc(mdb, 'Tiro', 10, 4, 5)
# found_chars = display_doc(mdb, 'Tiro')
# found_chars = display_id(mdb, "5e56fc630000b90542314c86")