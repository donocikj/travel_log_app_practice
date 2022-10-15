from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from auth_token.serializers import user_registration_deserializer
from auth_token.user import create_user

# Create your views here.

@api_view(["POST", "PUT"])
# /users/ - post - create user; put - update user?
def user_update_view(req):
    '''
    view for creating or updating new users
    '''
    if req.method == "POST":
        # create new user
        user_data = user_registration_deserializer(data=req.data)
        
        if not(user_data.is_valid()):
            # print(user_data.errors)
            return Response(data={"message":"invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        # todo: add try catch block
        new_user = create_user(user_data.validated_data)
        print(new_user)

        return Response(data={"created user id":new_user.id}, status=status.HTTP_201_CREATED)

    if req.method == "PUT":
        # update user
        user_data = user_registration_deserializer(data=req.data)

        return Response(data={"message":"updating user"}, status=status.HTTP_200_OK)

    else:
        # invalid request
        return Response(data={"message":"bad req"}, status=status.HTTP_400_BAD_REQUEST)

# /login/ - get - set up token as cookie

# /logout/ - get - clear token

# /auth/ - get - current auth information