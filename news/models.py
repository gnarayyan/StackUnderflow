from django.db import models
from users.models import User
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


class NewsModel(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    slug = models.CharField(max_length=150, blank=True, null=False)
    thubmnail = models.ImageField(upload_to='media/images/news', blank=True)
    content = models.TextField(blank=False, null=False)
    published_on = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    reading_time = models.IntegerField(default=5)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# class User:
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=150, blank=False, null=False)
#     last_name = models.CharField(max_length=150, blank=False, null=False)
#     avatar = models.ImageField(upload_to='media/images/user-profile')
