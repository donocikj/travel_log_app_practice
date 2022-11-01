from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Travel (models.Model):
    '''
    a collection of entries related to a particular trip by specific user
    '''
    traveller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return f'travel with id {self.id} submitted by {self.traveller}'


class Entry (models.Model):
    '''
    Entry of a travel log, related to a date, place and with text content; tied to a travel
    '''
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    # id within travel maybe?
    # entryid = models.IntegerField()
    location = models.CharField(max_length=50,blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    time = models.BigIntegerField(blank=True, null=True) #, default=int(datetime.now(timezone.utc).timestamp()))
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'entry from travel {self.travel},location: [{self.location}] absolute id: {self.id}'
