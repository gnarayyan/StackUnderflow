from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .utils import MODEL, SERIALIZER, NEWS_HELPER_MODELS
from rest_framework import generics
from rest_framework import filters
# Create your views here.
from rest_framework.filters import OrderingFilter, BaseFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models
########


class NewsHomeView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        print(request.GET.get('id'))  # query parameter
        return Response({
            'ENDPOINTS for info': [
                'api/news/info/language/',
                'api/news/info/region/',
                'api/news/info/category/',
                'api/news/info/section/'],
            'All news': [
                'api/news/info/language/',
                'api/news/info/region/',
                'api/news/info/category/',
                'api/news/info/section/'],
        })


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


class PostNewsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.PostNewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('News Added', status=status.HTTP_201_CREATED)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)


class NewsAllView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = models.NewsModel.objects.all()
    serializer_class = serializers.NewsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['author',
                        'category',
                        'language',
                        'published_on',
                        'region',
                        'section',
                        'slug']
    ordering_fields = ['author',
                       'category',
                       'language',
                       'published_on',
                       'region',
                       'section',
                       'slug', 'title']
    ordering = ['published_on']


class NewsAllSearchView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = models.NewsModel.objects.all()
    serializer_class = serializers.NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
