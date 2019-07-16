from rest_framework import serializers
from account.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','role','password' ,'is_active')
        extra_kwargs = {'password': {'write_only': True}}

    validate_password = make_password
