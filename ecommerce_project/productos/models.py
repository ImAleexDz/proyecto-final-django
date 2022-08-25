from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=40)
    price=models.FloatField()
    description=models.CharField(max_length=300, null=True, blank=True) 
    is_active=models.BooleanField(default=True)
    category=models.CharField(max_length=40)



