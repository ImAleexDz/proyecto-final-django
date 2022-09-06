from distutils.command.upload import upload
from os import name
from django.db import models
from categories.models import Category

class Products(models.Model):
    name=models.CharField(max_length=40)
    price=models.FloatField()
    description=models.CharField(max_length=300, null=True, blank=True) 
    is_active=models.BooleanField(default=False)
    category=models.CharField(max_length=40)
    image = models.ImageField(upload_to="products/", null=True, blank=True)

