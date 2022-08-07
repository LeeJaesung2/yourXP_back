from dataclasses import field
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate, login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'real_name', 'profile', 'nickname', 'email', 'point')

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)

        if user is None:
            return {
                'username': 'None'
            }
        login(request, user)
        return {
            'username': user.username
        }