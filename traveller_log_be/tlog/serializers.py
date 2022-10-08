from rest_framework import serializers

from tlog.models import Entry, Travel

class TravelSerializer(serializers.ModelSerializer):
    '''
    Serializer for travels.
    '''
    class Meta:
        model = Travel
        fields = '__all__'

class TravelDeserializer(serializers.ModelSerializer):
    '''
    deserializer for new or updated travels.
    '''
    # todo validate user existing - or leave it to the auth logic in endpoint?

class EntrySerializer(serializers.ModelSerializer):
    '''
    Serializer for individual entries.
    '''
    # todo: coordinate validation
    # todo: date and time validation
    class Meta:
        model = Entry
        fields = '__all__'