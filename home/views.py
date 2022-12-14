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
        return Response({'User EndPoints': {
            'Login User [POST]': 'api/users/login/',
            'Register User [POST]': 'api/users/register/',
            'Logout User [POST, use Token in HEADER]': 'api/auth/logout',
            'Get User Profile [GET, use Token in HEADER]': 'api/users/profile/'
        },
            'News EndPoints': {
            'All Avilable News [GET]': 'api/news/all/',
            'Filter News [GET]': 'api/news/all/?language=1',
            'Search News [GET]': 'api/news/?search=football',
            'Create News [GET]': 'api/news/post/',

        },
            'News Info EndPoints': {
            'All Avilable Languages [GET]': 'api/news/info/language',
            'All Avilable Regions [GET]': 'api/news/info/region',
            'All Avilable Categories [GET]': 'api/news/info/category',
            'All Avilable Sections [GET]': 'api/news/info/section'

        }
        })
