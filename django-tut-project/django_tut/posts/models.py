from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='owner',null=True)
    title = models.CharField(max_length=200,null=True)
    content = models.TextField(null=True,blank=True)
    attach = models.