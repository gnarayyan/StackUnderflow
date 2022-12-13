from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
# Create your models here.


class SectionModel(models.Model):
    #Breaking, Headline
    section = models.CharField(
        max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return self.section


class CategoryModel(models.Model):
    category = models.CharField(
        max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return self.category


class RegionModel(models.Model):
    region = models.CharField(
        max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return self.region


class LanguageModel(models.Model):
    language = models.CharField(
        max_length=30, blank=False, null=False, unique=True)

    def __str__(self):
        return self.language

# populate: python manage.py loaddata news.json


class NewsModel(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    language = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)
    reading_time = models.IntegerField(default=5)
    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, blank=True, null=False)
    thubmnail = models.ImageField(upload_to='images/news', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
