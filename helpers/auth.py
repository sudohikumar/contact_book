import jwt

SECRET_KEY = 'jswjIChMo6ED37Q33oGjGd0uquHettaz'


def encrypt_data(**kwargs):
    return jwt.encode(kwargs, SECRET_KEY, algorithm='HS256').decode('utf-8')


def decrypt_data(encoded_jwt):
    return jwt.decode(encoded_jwt, SECRET_KEY, algorithms=['HS256'])
