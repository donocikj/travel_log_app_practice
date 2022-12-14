from rest_framework import serializers

from tlog.models import Entry, Travel

class TravelSerializer(serializers.ModelSerializer):
    '''
    Serializer for travels.
    '''
    class Meta:
        model = Travel
        fields = '__all__'

class TravelDeserializer(serializers.Serializer):
    '''
    deserializer for new or updated travels.
    '''
    title = serializers.CharField(required=False)

class EntrySerializer(serializers.ModelSerializer):
    '''
    Serializer for individual entries.
    '''
    class Meta:
        model = Entry
        fields = '__all__'

class EntryDeserializer(serializers.Serializer):
    '''
    deserializer for creating or updating entries.
    '''
    # todo: coordinate validation?
    # todo: date and time validation
    # todo field length control?

    # this one is required for creation but not update...
    travel = serializers.IntegerField(required=False)

    location = serializers.CharField(required=False)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    time = serializers.IntegerField(required=False)
    content = serializers.CharField(required=False)