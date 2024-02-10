from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class user(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField() 
    profile_pic = models.ImageField(upload_to ='profile_pics')  

    def __str__(self):
        return self.name

