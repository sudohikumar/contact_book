from flask import Flask, jsonify, request

from connectors.connect import get_collection, get_mongo_client
from helpers.classes import config
from helpers.helpers import load_data
from mongo_helpers.operations import (delete_data, insert_data, read_data,
                                      update_data)

app = Flask(__name__)
app.config.from_json('config.json')

CLIENT = None
COLLECTION = None


@app.route('/getContacts', methods=['GET'], strict_slashes=False, defaults={'offset': 0, 'limit': 10})
@app.route('/getContacts/<offset>/', methods=['GET'], strict_slashes=False, defaults={'limit': 10})
@app.route('/getContacts/<offset>/<limit>', methods=['GET'], strict_slashes=False)
def getContacts(offset, limit):
    try:
        return jsonify(read_data(COLLECTION, int(offset), int(limit), **request.args))
    except Exception as e:
        return str(e)


@app.route('/createContact', methods=['POST'], strict_slashes=False)
def createContact():
    _data = request.get_json()
    response = None
    try:
        _data = load_data(_data)
        if not read_data(COLLECTION, 0, 1, email=_data.email):
            response = insert_data(COLLECTION, _data)
        else:
            raise ValueError('Email Already Exists')
    except Exception as e:
        return str(e)
    app.logger.info(f'Object ID: {str(response.inserted_id)}')
    return str(response.inserted_id)


@app.route('/updateContact/<id>', methods=['PUT'], strict_slashes=False)
def updateContact(id):
    _data = request.get_json()
    response = None
    try:
        _data = load_data(_data)
        response = update_data(COLLECTION, id, _data)
    except Exception as e:
        return str(e)

    if response.matched_count == 0:
        return 'No match found'
    return 'Success'


@app.route('/deleteContact/<id>', methods=['DELETE'], strict_slashes=False)
def deleteContact(id):
    response = None
    try:
        response = delete_data(COLLECTION, id)
    except Exception as e:
        return str(e)
    if response.deleted_count == 0:
        return 'No match found.'
    return 'Success'


if __name__ == '__main__':
    CLIENT = get_mongo_client(
        app.config['MONGO_HOST'], app.config['USERNAME'], app.config['PASSWORD'])
    COLLECTION = get_collection(
        CLIENT, app.config['DATABASE'], app.config['COLLECTION'])
    app.run(debug=True, host='0.0.0.0')
