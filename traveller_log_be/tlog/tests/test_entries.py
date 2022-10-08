'''
test for the entry model
'''

from tlog.views import entries_list_view

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

# test updating an entry - existing

# test updating an invalid entry

# test deleting an entry - existing

# test deleting an entry - invalid
