from django.db import models

# Create your models here.
class students (models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField (max_length=30)
    Phone = models.CharField (max_length=10)
    Password=models.CharField(max_length=15)    
    