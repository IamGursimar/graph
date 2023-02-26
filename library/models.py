from django.db import models

# Create your models here.

class Author(models.Model):
    family_name = models.CharField(max_length=250)
    given_name = models.CharField(max_length=250)

class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.DateField()
