'''
test for the travel model
'''
import json
from tlog.views import travels_list_view, travel_individual_view

from auth_token.utils import AUTH_COOKIE_KEY

# test listing with 1 fixture
def test_list_one_entry(rf, travel_sample):
    '''
    tries to call the get /tlog/travels/ endpoint with one entry in db
    '''
    request = rf.get('/tlog/travels/')

    response = travels_list_view(request)

    # assert response.data[0]['content'] == 'testcontent'
    # assert response.data[0]['location'] == 'testlocation'
    assert response.status_code == 200


# test listing empty db
def test_list_no_travel (db, rf):
    '''
    tries to call the get /tlog/travels/ endpoint with no travel in db
    '''
    request = rf.get('/tlog/travels/')

    response = travels_list_view(request)

    assert response.data == []
    assert response.status_code == 200

# test listing with filter

# test listing with invalid filter

# test creating new travel - valid
def test_create_travel_valid(rf, user_sample, user_sample_token):
    new_travel_data = json.dumps({
        "title":"new test travel"
    })

    request = rf.post('/tlog/travels/', new_travel_data, content_type='application/json')
    request.COOKIES[AUTH_COOKIE_KEY] = user_sample_token

    response = travels_list_view(request)

    assert response.status_code == 201
    # todo add assertion to find all travels by sample_user


# test creating new travel - invalid
def test_create_travel_invalid(rf, db):
    new_travel_data = json.dumps({
        "title":"new test travel by NN"
    })

    request = rf.post('/tlog/travels/', new_travel_data, content_type='application/json')

    response = travels_list_view(request)

    assert response.status_code == 401

# test retrieving individual travel with entries
def test_get_individual_travel(rf, travel_sample, entry_sample_1):

    request = rf.get(f'/tlog/travels/{travel_sample.id}/', content_type="application/json")

    response = travel_individual_view(request, travel_sample.id)

    assert response.status_code == 200
    # print(response.data)
    # todo check content of response


# test updating travel PUT /tlog/travels/{id}
def test_update_travel_title(rf, travel_sample, entry_sample_1, user_sample_token):
    update_data = json.dumps({
        "title":"updated title"
    })

    request = rf.put(f'/tlog/travels/{travel_sample.id}/', update_data, content_type="application/json")
    request.COOKIES[AUTH_COOKIE_KEY] = user_sample_token

    response = travel_individual_view(request, travel_sample.id)

    assert response.status_code == 200
    # todo check the new title


# test deleting travel DELETE /tlog/travels/{id}/
def test_delete_travel(rf, travel_sample, entry_sample_1, user_sample_token):

    request = rf.delete(f'/tlog/travels/{travel_sample.id}/', content_type="application/json")
    request.COOKIES[AUTH_COOKIE_KEY] = user_sample_token

    response = travel_individual_view(request, travel_sample.id)

    assert response.status_code == 200
    # todo check the travel is gone
