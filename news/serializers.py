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
        fields = ('id', 'category', 'ne', 'href')


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
                  'thumbnail',
                  'title')
        model = NewsModel

    author = UserSerializer()
    category = CategorySerializer()  # CategorySerializer()
    language = LanguageSerializer()  # LanguageSerializer()
    region = RegionSerializer()  # serializers.StringRelatedField()
    section = SectionSerializer()


class PostNewsSerializer(serializers.ModelSerializer):
    author = serializers.IntegerField()
    language = serializers.IntegerField()
    section = serializers.IntegerField()
    category = serializers.IntegerField()
    region = serializers.IntegerField()

    class Meta:
        model = NewsModel
        fields = ('author',
                  'language',
                  'section',
                  'category',
                  'region',
                  'content',
                  'reading_time',
                  'thumbnail',
                  'title')

    def create(self, validated_data):
        author_id = validated_data['author']
        author = User.objects.get(id=author_id)

        language_id = validated_data['language']
        language = LanguageModel.objects.get(id=language_id)

        category_id = validated_data['category']
        category = CategoryModel.objects.get(id=category_id)

        region_id = validated_data['region']
        region = RegionModel.objects.get(id=region_id)

        section_id = validated_data['section']
        section = SectionModel.objects.get(id=section_id)

        content = validated_data['content']
        reading_time = validated_data['reading_time']
        thumbnail = validated_data['thumbnail']
        title = validated_data['title']

        news = NewsModel.objects.create(
            author=author, language=language, category=category,
            section=section, region=region, content=content,
            reading_time=reading_time, thumbnail=thumbnail, title=title)
        news.save()

        return news  # super().create(validated_data)
