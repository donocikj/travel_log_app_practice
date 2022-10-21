from datetime import datetime, timedelta


import jwt

from django.contrib.auth.models import User
from traveller_log_be.settings import SECRET_KEY

# todo: move elsewhere
TOKEN_ALGORITHM = "HS256"
TOKEN_EXPIRATION = 120
AUTH_COOKIE_KEY = "indigo_token"

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

def decode_token(token):
    '''
    decodes token and returns its payload
    '''
    return jwt.decode(token, SECRET_KEY, algorithms=TOKEN_ALGORITHM)


def authenticate_request(request):
    '''
    checks request for cookies and returns User instance 
    if logged in, none if cookie is not set or is expired, 
    raises an exception in case of other problems.
    '''
    # retrieve token from cookie
    cookie = request.COOKIES.get("indigo_token")

    # check cookie
    if not cookie:
        return None

    # decode token
    try:
        payload = decode_token(cookie)
    except jwt.ExpiredSignatureError:
        # token expired
        return None
    except Exception as err:
        print(err)
        raise UserException("failed to decode cookie as valid") from err

    # retrieve the user object by id
    user = User.objects.filter(id=payload["user_id"]).first()

    # return
    return user

class UserException(Exception):
    '''
    custom user exception
    second verse same as the first
    '''

def refresh_token(user, response):
    '''
    function to refresh token cookie in the browser.
    Takes user object and a response object as parameter.
    '''
    payload = {
        "id": user.id,
        "username": user.username
    }
    token = encode_token(payload)
    response.set_cookie(key=AUTH_COOKIE_KEY, value=token, httponly=True)