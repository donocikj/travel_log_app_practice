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
    expects current credentials as two of the fields.
    '''
    # retrieve the user object to be updated
    modified_user = User.objects.filter(username=update_data.get('username')).first()
    
    if modified_user is None:
        # user specified doesn't exist
        raise UserException("user specified for updating does not exist")

    # check supplied password
    if not modified_user.check_password(update_data.get('password')):
        # password does not match the username
        raise UserException("authorization failure")

    # validate requested changes

    # username
    new_username = update_data.get('new_username')
    if new_username:
        if user_exists(username=new_username):
            raise UserException("username taken")
        else:
            modified_user.username = new_username

    # password
    new_password = update_data.get('new_password')
    if new_password:
        if len(new_password) < 8:
            raise UserException("sorry, your password is too short.")
        else:
            modified_user.set_password(new_password)

    # todo some loop with kwargs maybe? or would that be dangerous.
    # first name
    first_name = update_data.get('first_name')
    if first_name:
        modified_user.first_name = first_name

    # last name
    last_name = update_data.get('last_name')
    if last_name:
        modified_user.first_name = last_name

    # email
    email = update_data.get('email')
    if email:
        modified_user.first_name = email

    # apply changes
    # save
    modified_user.save()
    print("saved changes")

def prepare_token(creds):
    # check if user exists
    # check password match
    # (exception: wrong username or password)
    username = creds['username']
    password = creds['password']

    user = User.objects.filter(username=username).first()
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

