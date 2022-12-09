from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.


class RootHomeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({'Go to /api to view all Avilable API EndPoints'})


class APIHomeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({'User EndPoints': [
            'api/login',
            'api/logout',
            'api/signup',
            'api/profile'
        ]})
