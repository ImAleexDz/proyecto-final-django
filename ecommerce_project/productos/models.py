from unicodedata import name
from django.db import models

class productos(models.Model):
    name=models.CharField(max_length=40)
    price=models.FloatField()
    descreption=models.CharField(max_length=300, null=True, blank=True) 
    is_active=models.BooleanField(default=True)



