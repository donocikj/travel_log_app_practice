from datetime import datetime, timedelta


import jwt

from traveller_log_be.settings import SECRET_KEY

# todo: move elsewhere
TOKEN_ALGORITHM = "HS256"
TOKEN_EXPIRATION = 15

def generate_token(username):
    '''
    takes username and generates a token
    '''
    token = jwt.encode({
        "username":username,
        "exp":datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION),
        "iat":datetime.utcnow
        }, SECRET_KEY, algorithm=TOKEN_ALGORITHM)
    return token

def is_token_valid(token, username):
    '''
    decodes token and checks if username matches with claim
    '''
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=TOKEN_ALGORITHM)
        if payload.username == username:
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

