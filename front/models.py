from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField (max_length=200, unique= True)

    def __str__(self):
        return self.categoryname #Necessary for some reason but we'll figure out why in testing

class Article(models.model):
    title = models.CharField (max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    source = models.CharField (max_length=200, blank=True, null=True)
    pubdate = models.DateTimeField()
    content = models.TextField()