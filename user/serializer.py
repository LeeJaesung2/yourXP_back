from dataclasses import field
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'password', 'real_name', 'profile', 'nickname', 'email', 'point')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, user, validated_data):
        user.set_password(validated_data['password'])
        user.real_name = validated_data.get('real_name', user.real_name)
        user.profile = validated_data.get('profile', user.profile)
        user.nickname= validated_data.get('nickname', user.nickname)
        user.email= validated_data.get('email', user.email)
        user.save()
        return user