from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Travel (models.Model):
    '''
    a collection of entries related to a particular trip by specific user
    '''
    traveller = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'travel submitted by {self.traveller}'


class Entry (models.Model):
    '''
    Entry of a travel log, related to a date, place and with text content; tied to a travel
    '''
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    # id within travel maybe
    location = models.CharField(max_length=50)
    time = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return f'entry from travel {self.travel}'
