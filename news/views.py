from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.
from . import serializers
from . import models
########


class NewsHomeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        print(request.GET.get('id'))  # query parameter
        return Response({'News EndPoints': [
            'api/news',
        ]})


class InfoView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        queryset = {}
        serializer = {}
        queryset['language'] = models.LanguageModel.objects.all()
        queryset['region'] = models.RegionModel.objects.all()
        queryset['category'] = models.CategoryModel.objects.all()
        queryset['section'] = models.SectionModel.objects.all()

        serializer['language'] = serializers.LanguageSerializer(
            queryset['language'], many=True)
        serializer['region'] = serializers.RegionSerializer(
            queryset['region'], many=True)
        serializer['category'] = serializers.CategorySerializer(
            queryset['category'], many=True)
        serializer['section'] = serializers.SectionSerializer(
            queryset['section'], many=True)

        for k, v in serializer.items():
            serializer[k] = v.data
        return Response(serializer)
