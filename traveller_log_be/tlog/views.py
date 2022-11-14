from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from tlog.models import Entry, Travel
from tlog.serializers import EntryDeserializer, EntrySerializer, TravelSerializer, TravelDeserializer
from tlog.travel import create_travel, delete_travel, update_travel
from tlog.entry import create_entry, delete_entry, update_entry
from auth_token.utils import authenticate_request

# todo move constants to some centralized settings location
DEFAULT_RESULT_PAGE=10

# Create your views here.

def test_view(req):
    return HttpResponse("test view for the tlog")


# *********************************************************************************************
# entries views
# *********************************************************************************************


# /entries/ - GET list of entries
# /entries/ - POST new entry
@api_view(["GET", "POST"])
def entries_list_view(req):
    '''
    view to create, list or update individual entries
    '''
    if req.method == 'GET':

        # print(req)
        # print(dir(req))
        # print(req.query_params)
        # print(req.GET)
        # todo - filter feature

        requested_offset = req.query_params.get("from")
        if requested_offset is None:
            offset = 0
        else:
            try:
                offset = int(requested_offset)

            except ValueError:
                offset = 0

        requested_page_size = req.query_params.get("page")
        if requested_page_size is None:
            page_size = DEFAULT_RESULT_PAGE
        else:
            try:
                page_size = int(requested_page_size)

            except ValueError:
                page_size = DEFAULT_RESULT_PAGE

        
        try:
            entries = Entry.objects.all()[offset:offset+page_size]
        except ValueError:
            return Response(data={"message":"negative indexing is not supported"}, status=status.HTTP_400_BAD_REQUEST)


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

        # print(entry_data.validated_data)
        # check if travel is authored by the logged in user
        # todo maybe refactor this logic to the create_entry function and put call in try block
        travel_id = entry_data.validated_data.get("travel")
        if not travel_id:
            return Response(data={"error":"invalid input: travel unspecified"}, status=status.HTTP_400_BAD_REQUEST)

        travel = Travel.objects.filter(id=travel_id).first()

        # print("travel")
        # print(travel)

        if travel is None:
            return Response(data={"error":"invalid travel"}, status=status.HTTP_400_BAD_REQUEST)
        
        if travel.traveller.id != logged_user.id:
            return Response(data={"error":"travel does not belong to logged in user"}, status=status.HTTP_403_FORBIDDEN)

        new_entry = create_entry(entry_data.validated_data, travel)

        return Response(data={"message":"creating new entry", "id":new_entry.id }, status=status.HTTP_201_CREATED)

    return Response(data={"message":"method not supported"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(["GET", "PUT", "DELETE"])
def entry_individual_view(req, id):
    '''
    view to handle individual travel entries
    GET specific entry
    PUT update an entry
    DELETE remove an entry
    '''

    selected_entry = Entry.objects.filter(id=id).first()

    if selected_entry is None:
        return Response(data={"message":"entry not found", "id":id}, status=status.HTTP_404_NOT_FOUND)

    # auth not required in this case
    if req.method == 'GET':
        entry_serializer = EntrySerializer(selected_entry)
        return Response(data=entry_serializer.data, status=status.HTTP_200_OK)

    # auth
    logged_user = authenticate_request(req)

    if not logged_user:
        return Response(data={"error":"missing authentication"}, status=status.HTTP_401_UNAUTHORIZED)

    # check authorization of logged in user
    if logged_user.id != selected_entry.travel.traveller.id:
        return Response(data={"message":"entry does not belong to logged in user", "id":id}, status=status.HTTP_403_FORBIDDEN)

    if req.method == 'PUT':
        update_data = EntryDeserializer(data=req.data)

        if not update_data.is_valid():
            print(update_data.errors)
            return Response(data={"message":"failed to update - invalid input", "id":id}, status=status.HTTP_400_BAD_REQUEST)

        update_entry(update_data.validated_data, selected_entry)
        return Response(data={"message":"updating entry", "id":id}, status=status.HTTP_200_OK)

    if req.method == 'DELETE':
        delete_entry(selected_entry)
        return Response(data={"message":"deleting entry", "id":id}, status=status.HTTP_200_OK)

    return Response(data={"message":"method not supported"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED)


# *********************************************************************************************
# travels views
# *********************************************************************************************


# /travels/ - GET list of trips, POST create new trip
@api_view(["GET", "POST"])
def travels_list_view(req):
    '''
    view to create (POST) or list (GET) travel objects, with optional filtering by query string
    '''
    # todo: only allow authenticated request to POST
    # todo: everything

    if req.method == 'GET':


        #pagination
        # todo: filters 
        requested_offset = req.query_params.get("from")
        if requested_offset is None:
            offset = 0
        else:
            try:
                offset = int(requested_offset)

            except ValueError:
                offset = 0

        requested_page_size = req.query_params.get("page")
        if requested_page_size is None:
            page_size = DEFAULT_RESULT_PAGE
        else:
            try:
                page_size = int(requested_page_size)

            except ValueError:
                page_size = DEFAULT_RESULT_PAGE

        
        try:
            travels = Travel.objects.all()[offset:offset+page_size]
        except ValueError:
            return Response(data={"message":"negative indexing is not supported"}, status=status.HTTP_400_BAD_REQUEST)



        # travels = Travel.objects.all()
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
@api_view(['GET', 'PUT', 'DELETE'])
def travel_individual_view(req, id):
    '''
    view pertaining to individual travel object
    GET: retrieve particular travel and its entries
    PUT: update travel data (title)
    DELETE: remove the travel and its entries
    '''

    # retrieve travel by id in path param
    selected_travel = Travel.objects.filter(id=id).first()

    if selected_travel is None:
        return Response(data={"message":"travel not found", "id":id}, status=status.HTTP_404_NOT_FOUND)

    # no login required for GETting...
    if req.method == 'GET':
        # retrieve entries
        entries = Entry.objects.filter(travel=selected_travel.id)

        # put object together and return
        full_travel = {
            'travel':TravelSerializer(selected_travel).data,
            'entries':EntrySerializer(entries, many=True).data
        }
        return Response(data=full_travel, status=status.HTTP_200_OK)

    # authenticate
    logged_user = authenticate_request(req)

    if not logged_user:
        return Response(data={"error":"missing authentication"}, status=status.HTTP_401_UNAUTHORIZED)

    # check authorization of logged in user
    if selected_travel.traveller.id != logged_user.id:
        return Response(data={"message":"travel does not belong to logged in user", "id":id}, status=status.HTTP_403_FORBIDDEN)

    if req.method == 'PUT':

        update_data = TravelDeserializer(data=req.data)

        if not update_data.is_valid():
            print(update_data.errors)
            return Response(data={"message":"failed to update - invalid input", "id":id}, status=status.HTTP_400_BAD_REQUEST)
            
        update_travel(update_data.validated_data, selected_travel)

        return Response(data={"message":"updating travel", "id":id}, status=status.HTTP_200_OK)

    if req.method == 'DELETE':

        delete_travel(selected_travel)

        return Response(data={"message":"deleting travel", "id":id}, status=status.HTTP_200_OK)