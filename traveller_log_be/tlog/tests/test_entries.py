'''
test for the entry model
'''

from tlog.views import entries_list_view, entry_individual_view
from auth_token.utils import AUTH_COOKIE_KEY

# test listing with 1 fixture
def test_list_one_entry(rf, entry_sample_1):
    '''
    tries to call the get /tlog/entries/ endpoint with one entry in db
    '''
    request = rf.get('/tlog/entries/')

    response = entries_list_view(request)

    assert response.data[0]['content'] == 'testcontent'
    assert response.data[0]['location'] == 'testlocation'
    assert response.status_code == 200


# test listing empty db
def test_list_no_entry(db, rf):
    '''
    tries to call the get /tlog/entries/ endpoint with no entry in db
    '''
    request = rf.get('/tlog/entries/')

    response = entries_list_view(request)

    assert response.data == []
    assert response.status_code == 200

# test listing with filter

# test listing with invalid filter

# test creating new entry
def test_create_entry(rf, travel_sample, user_sample_token):
    '''
    /tlog/entries/ post - create entry for a travel.
    '''
    new_entry_data = {
        "travel": travel_sample.id,
        "location": "somewhere",
        "latitude": 0.0,
        "longitude": 0.0,
        "time": 1,
        "content": "test entry"
    }

    request = rf.post('/tlog/entries/', new_entry_data, content_type="application/json")
    request.COOKIES[AUTH_COOKIE_KEY] = user_sample_token

    response = entries_list_view(request)

    assert response.status_code == 201


# test updating an entry - existing
def test_update_existing_entry(rf, entry_sample_1, user_sample_token):
    '''
    /tlog/entries/<id>/ PUT - update an entry
    '''
    update_entry_data = {
        "content":"new content"
    }

    request = rf.put(f'/tlog/entries/{entry_sample_1.id}/', update_entry_data, content_type="application/json")
    request.COOKIES[AUTH_COOKIE_KEY] = user_sample_token

    response = entry_individual_view(request, entry_sample_1.id)

    assert response.status_code == 200
    # todo check updated content


# test updating an invalid entry
def test_update_existing_entry(rf, user_sample_token):
    '''
    /tlog/entries/<id>/ PUT - update an entry
    '''
    update_entry_data = {
        "content":"new content"
    }

    bogus_id = 13

    request = rf.put(f'/tlog/entries/{bogus_id}/', update_entry_data, content_type="application/json")
    request.COOKIES[AUTH_COOKIE_KEY] = user_sample_token

    response = entry_individual_view(request, bogus_id)

    assert response.status_code == 404
    # todo check updated content

# test deleting an entry - existing
def test_deleting_existing_entry(rf, entry_sample_1, user_sample_token):
    '''
    /tlog/entries/<id>/ DELETE - remove an entry
    '''
    request = rf.delete(f'/tlog/entries/{entry_sample_1.id}/')
    request.COOKIES[AUTH_COOKIE_KEY] = user_sample_token

    response = entry_individual_view(request, entry_sample_1.id)

    assert response.status_code == 200

    # todo check the entry is gone


# test deleting an entry - invalid
def test_deleting_existing_entry(rf, user_sample_token):
    '''
    /tlog/entries/<id>/ DELETE - remove an entry
    '''

    bogus_id = 13

    request = rf.put(f'/tlog/entries/{bogus_id}/')
    request.COOKIES[AUTH_COOKIE_KEY] = user_sample_token

    response = entry_individual_view(request, bogus_id)

    assert response.status_code == 404
    