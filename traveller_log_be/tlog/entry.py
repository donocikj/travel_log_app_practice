'''
this module should contain logic handling individual travel log entries
'''
from tlog.models import Entry


def create_entry(entry_data, travel):
    '''
    creates new entry with values given in 'entry_data' argument 
    and saves it under travel supplied as the second argument.
    '''
    entry_fields = {**entry_data.validated_data}
    # print (entry_fields)
    entry_fields['travel'] = travel
    # print (entry_fields)
    
    return Entry.objects.create(**entry_fields)

def update_entry(entry_data, entry):
    pass

def delete_entry(entry):
    pass