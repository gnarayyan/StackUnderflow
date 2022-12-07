from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import SignupSerializer, LoginSerializer
from django.contrib.auth import authenticate
# Create your views here.


class Signup(APIView):
    def get(self, request):
        return Response({'username': '', 'first_name': '', 'last_name': '', 'password': '', 'email': '', 'avatar': 'This is an image Field'})

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'User Created'}, status=status.HTTP_201_CREATED)


##### TEST ######
class Login(APIView):
    def get(self, request):
        return Response({'username': '',  'password': ''})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username, password = serializer.data['username'], serializer.data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'Logined Succesfully'})
        else:
            return Response({'Cannot authenticated with the credentials'})
#########


@api_view(['GET'])
def login(request):
    return Response('OK')


@api_view(['GET'])
def logout(request):
    # auth.logout(request)
    return Response('DONE')
