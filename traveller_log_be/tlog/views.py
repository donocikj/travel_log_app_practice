from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from tlog.models import Entry, Travel
from tlog.serializers import EntrySerializer, TravelSerializer

# Create your views here.

def test_view(req):
    return HttpResponse("test view for the tlog")


# /entries/ - GET list of entries
# /entries/ - POST new entry
@api_view(["GET", "POST"])
def entries_list_view(req):
    '''
    view to create, list or update individual entries
    '''
    if req.method == 'GET':
        # todo - filter feature
        entries = Entry.objects.all()
        entry_serializer = EntrySerializer(entries, many=True)
        return Response(data=entry_serializer.data, status=status.HTTP_200_OK)
        # return Response(data={"message":"listing all entries"}, status=status.HTTP_200_OK)
    if req.method == 'POST':
        return Response(data={"message":"creating new entry"}, status=status.HTTP_201_CREATED)

    return Response(data={"message":"method not supported"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED)

# /entries/{id} - GET specific entry
# /entries/{id} - PUT update an entry
# /entries/{id} - DELETE remove an entry


# /travels/ - GET list of trips, POST create new trip
@api_view(["GET", "POST"])
def travels_list_view(req):
    '''
    view to create (POST) or list (GET) travel objects, with optional filtering by query string
    '''
    # todo: only allow authenticated request to POST
    # todo: everything

    if req.method == 'GET':
        travels = Travel.objects.all()
        travel_serializer = TravelSerializer(travels, many=True)
        print(travel_serializer.data)
        return Response(data=travel_serializer.data, status=status.HTTP_200_OK)
        # return Response(data={"message":"listing all travels"}, status=status.HTTP_200_OK)

    if req.method == 'POST':
        return Response(data={"message":"creating new travel"}, status=status.HTTP_201_CREATED)

    return Response(data={"message":"method not supported"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED)

# /travels/{id} - GET, PUT, DELETE