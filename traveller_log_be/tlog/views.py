from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from tlog.models import Entry, Travel
from tlog.serializers import EntryDeserializer, EntrySerializer, TravelSerializer, TravelDeserializer
from tlog.travel import create_travel
from tlog.entry import create_entry
from auth_token.utils import authenticate_request

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

        # authenticate user
        logged_user = authenticate_request(req)

        if not logged_user:
            return Response(data={"error":"missing authentication"}, status=status.HTTP_401_UNAUTHORIZED)

        entry_data = EntryDeserializer(data=req.data)

        if not entry_data.is_valid():
            return Response(data={"error":"invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        print(entry_data.validated_data)
        # check if travel is authored by the logged in user
        # todo maybe refactor this logic to the create_entry function and put call in try block
        travel = Travel.objects.filter(id=entry_data.validated_data.get("travel")).first()
        print("travel")
        print(travel)

        if travel is None:
            return Response(data={"error":"invalid travel"}, status=status.HTTP_400_BAD_REQUEST)
        
        if travel.traveller.id != logged_user.id:
            return Response(data={"error":"travel does not belong to logged in user"}, status=status.HTTP_403_FORBIDDEN)

        new_entry = create_entry(entry_data, travel)

        return Response(data={"message":"creating new entry", "id":new_entry.id }, status=status.HTTP_201_CREATED)

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
        # print(travel_serializer.data)
        return Response(data=travel_serializer.data, status=status.HTTP_200_OK)
        # return Response(data={"message":"listing all travels"}, status=status.HTTP_200_OK)

    if req.method == 'POST':

        # authenticate user
        logged_user = authenticate_request(req)

        if not logged_user:
            return Response(data={"error":"missing authentication"}, status=status.HTTP_401_UNAUTHORIZED)

        new_travel_data = TravelDeserializer(data=req.data)

        if not new_travel_data.is_valid():
            print(new_travel_data.errors)
            # it's literally just the title field which is not even mandatory
            return Response(data={"error":"I have no idea how you managed that tbh"}, status=status.HTTP_400_BAD_REQUEST)

        new_travel = create_travel(new_travel_data.validated_data, logged_user)

        return Response(data={"message":"creating new travel", "id":new_travel.id}, status=status.HTTP_201_CREATED)

    return Response(data={"message":"method not supported"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED)

# /travels/{id} - GET, PUT, DELETE