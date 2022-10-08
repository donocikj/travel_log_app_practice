from rest_framework.decorators import api_view


# Create your views here.

@api_view(["POST", "PUT"])
# /users/ - post - create user; put - update user?
def user_update_view(req):
    '''
    view for creating or updating new users
    '''
    if req.method == "POST":
        # create new user
        return Response(data={"message":"creating new user"}, status=status.HTTP_200_OK)
    if req.method == "PUT":
        # update user
        return Response(data={"message":"updating user"}, status=status.HTTP_200_OK)
    else:
        # invalid request
        return Response(data={"message":"bad req"}, status=status.HTTP_400_BAD_REQUEST)

# /login/ - get

# /auth/ - get