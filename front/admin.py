from django.contrib import admin
from . import models

# Register your models here.s
admin.site.register(models.Category)
admin.site.register(models.Article)