from rest_framework import serializers

class User_update_deserializer(serializers.Serializer):
    '''
    Deserializer for user registration requests
    '''
    username = serializers.CharField(required=False)
    new_username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    new_password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    
    # todo: validate password length?

class Credentials_deserializer(serializers.Serializer):
    '''
    deserializer for the login endpoint
    '''
    username = serializers.CharField()
    password = serializers.CharField()