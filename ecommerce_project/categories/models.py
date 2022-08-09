from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    keywords = models.CharField(max_length=50)
