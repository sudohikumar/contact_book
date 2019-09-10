import urllib

from pymongo import MongoClient


def get_mongo_client(connect_url, username, password):
    CONENCT_URL = f'mongodb+srv://{urllib.parse.quote(username)}:{urllib.parse.quote(password)}@{connect_url}/test?retryWrites=true&w=majority'
    return MongoClient(CONENCT_URL)


def get_collection(client, db, collection):
    return client[db][collection]
