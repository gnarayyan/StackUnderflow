from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .utils import MODEL, SERIALIZER, NEWS_HELPER_MODELS
# Create your views here.
from . import serializers
from . import models
########


class NewsHomeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        print(request.GET.get('id'))  # query parameter
        return Response({'News EndPoints': [
            'api/news/info/'],
            'UPDATED ENDPOINTS for info': [
                'api/news/info/language/',
                'api/news/info/region/',
                'api/news/info/category/',
                'api/news/info/section/'],
        })


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


class CategoryView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, model: str):
        if model not in NEWS_HELPER_MODELS:
            return Response({'Error ❌': f'api/news/info/{model} is not a valid endpoint'},
                            status=status.HTTP_404_NOT_FOUND)

        queryset = MODEL[model].objects.all()

        serializer = SERIALIZER[model](
            queryset, many=True)
        return Response(serializer.data)
