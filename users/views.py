from rest_framework import permissions, views, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login, logout
from . import serializers

# Create your views here.


class Signup(APIView):
    def get(self, request):
        return Response({'username': '', 'first_name': '', 'last_name': '', 'password': '', 'email': '', 'avatar': 'This is an image Field'})

    def post(self, request):
        serializer = serializers.SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'User Created'}, status=status.HTTP_201_CREATED)


##### TEST ######
'''
class Login(APIView):
    def get(self, request):
        return Response({'username': '',  'password': ''})

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username, password = serializer.data['username'], serializer.data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'Logined Succesfully'})
        else:
            return Response({'Cannot authenticated with the credentials'})'''

# new
# https://www.guguweb.com/2022/01/23/django-rest-framework-authentication-the-easy-way/


class DataView(views.APIView):
    def get(self, request):
        return Response({'Authenticated'})


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserProfileSerializer

    def get_object(self):

        return self.request.user


class LoginView(views.APIView):
    # parser_classes = [JSONParser]  # , JSONParser,
    # FormParser, MultiPartParser, FileUploadParser]
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({'username': '', 'password': ''})

    def post(self, request):
        print('Header: ', request.headers)
        serializer = serializers.LoginSerializer(
            data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)
        return Response({'Succesfully Login'}, status=status.HTTP_202_ACCEPTED)


class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request)
        print(dir(request))
        logout(request)
        return Response({'detail': 'Successfully Logout'}, status=status.HTTP_200_OK)
