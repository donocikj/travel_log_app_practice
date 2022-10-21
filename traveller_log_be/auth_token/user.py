from django.contrib.auth.models import User
from auth_token.utils import UserException, encode_token

# maybe switch to id?
def user_exists(username):
    return User.objects.filter(username=username).exists()

def create_user(user_data):
    '''
    take object deserialized from request, validate it and, 
    if everything is fine, add them to database.
    '''
    
    # check username - is valid?
    if not user_data.get('username'):
        raise UserException("username missing or blank")

    # check username - exists?
    if user_exists(user_data.get('username')):
        raise UserException("username already taken")

    # check password - is valid?
    if not user_data.get('password') or len(user_data.get('password')) < 8:
        raise UserException("password too short or missing")

    # special treatment for fields: id, is_staff, is_active, is_superuser, date_joined?

    # create new user
    return User.objects.create_user(**user_data)
    # return None

# todo
def update_user(update_data):
    '''
    take object deserialized from request, validate and update fields
    '''
    # retrieve the user object to be updated
    # validate requested changes?
    # apply changes
    # save

def prepare_token(creds):
    # check if user exists
    # check password match
    # (exception: wrong username or password)
    username = creds['username']
    password = creds['password']

    user = User.objects.get(username=username)
    if not user or not password or not user.check_password(password):
        raise UserException("incorrect username or password")

    # create token with creds
    payload = {
        "id": user.id,
        "username": username
    }
    token = encode_token(payload)

    # return token
    return token

