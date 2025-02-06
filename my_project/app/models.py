from django.db import models
class register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    
class products(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.CharField(max_length=50)
    
# Create your models here.
