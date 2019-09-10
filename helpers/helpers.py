import json
import re

from helpers.classes import contacts_data


def load_data(data):
    data = contacts_data.from_json(json.dumps(data))
    verify_data(data)
    return data


def verify_data(data):
    res = {'code': 0, 'message': ''}
    if verify_email(data.email)[0] == 0:
        raise ValueError(verify_email(data.email)[1])
    if data.name == '':
        raise ValueError('Name should not be empty.')
    if int(data.phone) and len(data.phone) != 10:
        raise ValueError('Phone Number not valid')


def verify_email(addressToVerify):
    match = re.match(
        '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)
    if match == None:
        return (0, 'Not a valid email')
    else:
        return (1, 'Valid Email')
