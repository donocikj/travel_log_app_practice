'''
this file should house functions invoked by the endpoints that access Travel objects...
'''

from tlog.models import Travel



def create_travel(travel_data, user):
    # todo maybe check if user is allowed to create new travels

    title = travel_data.get('title')
    # if title is blank, make a default one
    if not title:
        title = f"{user.username}'s travel"

    # todo catch exceptions? Or let the caller handle them.
    return Travel.objects.create(traveller=user, title=title)

def update_travel():
    pass

def delete_travel():
    pass