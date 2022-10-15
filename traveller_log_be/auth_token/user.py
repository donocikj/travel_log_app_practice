from django.contrib.auth.models import User

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
        raise Exception("username missing or blank")

    # check username - exists?
    if user_exists(user_data.get('username')):
        raise Exception("username already taken")

    # check password - is valid?
    if not user_data.get('password') or len(user_data.get('password')) < 8:
        raise Exception("password too short or missing")

    # special treatment for fields: id, is_staff, is_active, is_superuser, date_joined?

    # create new user
    return User.objects.create_user(**user_data)
    # return None

# todo
def update_user(update_data):
    '''
    take object deserialized from request, validate and update fields
    '''
    # check username validity and availability
    # check validity of other fields
    # special treatment for password?