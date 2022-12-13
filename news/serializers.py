from rest_framework import serializers
from .models import SectionModel, CategoryModel, RegionModel, LanguageModel, NewsModel

from django.contrib.auth.models import User
from users.serializers import UserSerializer


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionModel
        fields = ('id', 'section',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'category',)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionModel
        fields = ('id', 'region',)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = ('id', 'language',)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('author',
                  'category',
                  'content',
                  'language',
                  'published_on',
                  'reading_time',
                  'region',
                  'section',
                  'slug',
                  'thubmnail',
                  'title')
        model = NewsModel

    author = UserSerializer()
    category = CategorySerializer()  # CategorySerializer()
    language = LanguageSerializer()  # LanguageSerializer()
    region = RegionSerializer()  # serializers.StringRelatedField()
    section = SectionSerializer()
