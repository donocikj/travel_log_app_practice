'''
test for the travel model
'''

from tlog.views import travels_list_view

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

# test creating new travel
