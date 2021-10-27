from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    stat = [
        ('On','online'),
        ('Bu','bussy'),
        ('Of','offline')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=2, choices=stat, null=True, blank=True)
    bio = models.CharField(max_length=400, null=True, blank=True)
    profile_pic = models.ImageField(null=True,blank=True)