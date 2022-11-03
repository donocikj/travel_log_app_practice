'''
this module should contain logic handling individual travel log entries
'''
from tlog.models import Entry


def create_entry(entry_data, travel):
    '''
    creates new entry with values given in 'entry_data' argument 
    and saves it under travel supplied as the second argument.
    '''
    entry_fields = {**entry_data}
    # print (entry_fields)
    entry_fields['travel'] = travel
    # print (entry_fields)
    
    return Entry.objects.create(**entry_fields)

# todo move this stuff to serializers
def update_entry(entry_data, entry):
    # travel? (move to another travel by the same owner?)
    # location
    if entry_data.get('location'):
        entry.location = entry_data['location']

    # latitude
    if entry_data.get('latitude'):
        entry.latitude = entry_data['latitude']
    # longitude
    if entry_data.get('longitude'):
        entry.longitude = entry_data['longitude']
    # time?
    if entry_data.get('time'):
        entry.time = entry_data['time']
    # content
    if entry_data.get('content'):
        entry.content = entry_data['content']

    entry.save()
    return entry

def delete_entry(entry):
    entry.delete()
