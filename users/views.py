
# import
from django.contrib.auth import login
from django.contrib.auth.models import User
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer, RegisterSerializer
# Signup


# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Class based view to register user


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
# Login


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response('get')

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
