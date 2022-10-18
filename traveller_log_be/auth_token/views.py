from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from auth_token.serializers import User_registration_deserializer
from auth_token.user import create_user, prepare_token, update_user
from auth_token.utils import UserException, authenticate_request

# Create your views here.

@api_view(["POST", "PUT"])
# /users/ - post - create user; put - update user?
def user_update_view(req):
    '''
    view for creating or updating new users
    '''
    if req.method == "POST":
        # create new user
        user_data = User_registration_deserializer(data=req.data)
        
        if not(user_data.is_valid()):
            # print(user_data.errors)
            return Response(data={"message":"invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        # todo: add try catch block
        try:
            new_user = create_user(user_data.validated_data)
        except UserException as err:
            return Response(data={"message":str(err)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(err)
            return Response(data={"message":"internal error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # print(new_user)

        return Response(data={"created user id":new_user.id}, status=status.HTTP_201_CREATED)

    if req.method == "PUT":

        # authenticate user

        # update user
        user_data = User_registration_deserializer(data=req.data)

        if not(user_data.is_valid()):
            # print(user_data.errors)
            return Response(data={"message":"invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        update_user(user_data)

        return Response(data={"message":"updating user"}, status=status.HTTP_200_OK)

    else:
        # invalid request
        return Response(data={"message":"bad req"}, status=status.HTTP_400_BAD_REQUEST)

# /login/ - post - set up token as cookie
@api_view(["POST"])
def login_view(req):
    '''
    accepts username and password, sets up token in response.
    '''

    try:
        # call token creating function
        print(req.data)
        token = prepare_token(req.data)
    except UserException as err:
        return Response(data={"message":str(err)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(data={"message":"internal error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    print(token)
    print(dir(token))
    response = Response(data={"logged in":"success"}, status=status.HTTP_200_OK)
    response.set_cookie(key="indigo_token",value=token, httponly=True)

    return response
    

# /logout/ - post - clear token
@api_view(["GET"])
def logout_view(req):
    '''
    clears token from the browser
    '''

# /auth/ - get - current auth information
@api_view(["GET"])
def auth_view(req):
    '''
    get auth information based on token so the frontend is told who is it servicing
    '''

    #validate token - failure: nobody is logged int
    try:
        user = authenticate_request(req)
    except UserException as err:
        print(err)
        return Response(data={"message":str(err)}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(data={"id": user.id, "username": user.username }, status=status.HTTP_200_OK)


    # success: return {user_id, username}