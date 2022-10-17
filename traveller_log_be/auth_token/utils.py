from datetime import datetime, timedelta


import jwt

from traveller_log_be.settings import SECRET_KEY

# todo: move elsewhere
TOKEN_ALGORITHM = "HS256"
TOKEN_EXPIRATION = 15

def encode_token(payload):
    '''
    takes username and generates a token
    '''
    print("preparing to encode")
    # print(payload)
    # user_id = payload["id"]
    # username = payload["username"]
    token = jwt.encode({
        "user_id":payload['id'],
        "username":payload['username'],
        "exp":datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION),
        "iat":datetime.utcnow()
        }, SECRET_KEY, algorithm=TOKEN_ALGORITHM)
    print(token)
    return token

def is_token_valid(token, id):
    '''
    decodes token and checks if id matches with claim
    '''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=TOKEN_ALGORITHM)
        if payload.id == id:
            return True
        else:
            return False
    except Exception as err:
        print(err)
        return False

def is_request_valid(request):
    '''
    checks request for cookies
    '''

class UserException(Exception):
    '''
    custom user exception
    second verse same as the first
    '''