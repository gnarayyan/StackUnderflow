from rest_framework import serializers
from .models import SectionModel, CategoryModel, RegionModel, LanguageModel, NewsModel


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionModel
        fields = ('section',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('category',)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionModel
        fields = ('region',)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageModel
        fields = ('language',)


class InfoSerializer(serializers.Serializer):
    language = LanguageSerializer(read_only=True, many=True)
    region = RegionSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True, many=True)
    section = SectionSerializer(read_only=True, many=True)
