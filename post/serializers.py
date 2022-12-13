from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# Serializer to Get User Details using Django Token Authentication


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "username"]

# Serializer to Register User


class RegisterSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    full_name = serializers.CharField(
        max_length=256, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'full_name')
        # 'email')   , 'first_name', 'last_name')
        # extra_kwargs = {
        #     'first_name': {'required': True},
        #     'last_name': {'required': True}
        # }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        full_name = validated_data['full_name'].split(' ')
        user = User.objects.create(
            username=validated_data['username'],
            # email=validated_data['email'],
            first_name=full_name[0],
            last_name=full_name[1]
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
