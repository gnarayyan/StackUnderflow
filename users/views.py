
# import
from django.contrib.auth import login
from django.contrib.auth.models import User
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
from users.serializers import UserSerializer, RegisterSerializer
# UserProfile


# class LoginView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = (UserSerializer,)

#     def get(self, request):
#         return Response('Do a post request')

#     def post(self, request, format=None):
#         # serializer = AuthTokenSerializer(data=request.data)
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'user': user, 'token': str(token)}, status=status.HTTP_200_OK)
#         # return super(LoginView, self).post(request, format=None)

from knox.auth import TokenAuthentication as TK


class UserProfile(APIView):
    authentication_classes = (TK,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        print(self.request.user)
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

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
        return Response('Do a post request')

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
