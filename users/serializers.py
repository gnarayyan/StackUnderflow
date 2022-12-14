
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]

# Serializer to Register User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    full_name = serializers.CharField(
        max_length=256, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'full_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        full_name = validated_data['full_name'].split(' ')
        user = User.objects.create(
            username=validated_data['username'],
            first_name=full_name[0],
            last_name=full_name[1]
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
