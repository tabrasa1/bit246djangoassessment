from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField (max_length=200, unique= True)

    def __str__(self):
        return self.categoryName #Labels with readable name in the admin dropdowns instead of "Category object (1)"

class Article(models.Model):
    title = models.CharField (max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    source = models.CharField (max_length=200, blank=True, null=True)
    pubdate = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.title