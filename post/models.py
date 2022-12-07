from django.db import models
from users.models import User
from slugify import slugify
# Create your models here.


class LanguageModel(models.Model):
    language = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.language


class PostModel(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    slug = models.CharField(max_length=150, blank=True, null=False)
    poster = models.ImageField(upload_to='media/images/post')
    content = models.TextField(blank=False, null=False)

    modified_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Publish(models.IntegerChoices):
        PUBLISH = 0
        DRAFT = 1
    publish = models.IntegerField(choices=Publish.choices)

    author = models.OneToOneField(User, on_delete=models.PROTECT)
    language = models.OneToOneField(LanguageModel, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
