from rest_framework import serializers

from django.conf.global_settings import AUTH_USER_MODEL
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email',
                  'first_name', 'last_name', 'avatar')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(
#         max_length=150, min_length=4, allow_blank=False, trim_whitespace=True)
#     password = serializers.CharField(
#         max_length=150, min_length=4, allow_blank=False, trim_whitespace=True)
