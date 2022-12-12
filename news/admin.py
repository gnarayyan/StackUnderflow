from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CategoryModel)
admin.site.register(models.LanguageModel)
admin.site.register(models.NewsModel)
admin.site.register(models.RegionModel)
admin.site.register(models.SectionModel)
