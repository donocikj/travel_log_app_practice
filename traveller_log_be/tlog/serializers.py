from rest_framework import serializers

from tlog.models import Entry, Travel

class TravelSerializer(serializers.ModelSerializer):
    '''
    Serializer for travels.
    '''
    class Meta:
        model = Travel
        fields = '__all__'

class EntrySerializer(serializers.ModelSerializer):
    '''
    Serializer for individual entries.
    '''
    # todo: coordinate validation
    # todo: date and time validation
    class Meta:
        model = Entry
        fields = '__all__'