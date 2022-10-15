from rest_framework import serializers

class user_registration_deserializer(serializers.Serializer):
    '''
    Deserializer for user registration requests
    '''
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    
    # todo: validate password length?