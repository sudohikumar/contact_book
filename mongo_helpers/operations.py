import json

from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import ASCENDING, MongoClient

from helpers.classes import contacts_data


def read_data(collection, offset, limit, **kwargs):
    return json.loads(dumps(collection.find(kwargs).skip(offset).sort('_id', ASCENDING).limit(limit)))


def insert_data(colletion, data):
    data = contacts_data.to_json(data)
    return colletion.insert_one(json.loads(data))


def update_data(collection, object_id, data):
    data = contacts_data.to_json(data)
    obj = {'_id': ObjectId(
        object_id['$oid']) if '$oid' in object_id else ObjectId(object_id)}
    data = {'$set': json.loads(data)}
    return collection.update_one(obj, data)


def delete_data(collection, object_id):
    return collection.delete_one({'_id': ObjectId(object_id)})
