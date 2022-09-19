from django.http import HttpResponse

# Create your views here.

def test_view(req):
    return HttpResponse("test view for the tlog")


# to be moved elsewhere
# /login/ - get
# /auth/ - get
# /users/ - post - create user; put - update user?


# /entries/ - GET list of entries
# /entries/ - POST new entry
# /entries/{id} - GET specific entry
# /entries/{id} - PUT update an entry
# /entries/{id} - DELETE remove an entry

# /travels/ - GET list of trips, POST create new trip
# /travels/{id} - GET, PUT, DELETE