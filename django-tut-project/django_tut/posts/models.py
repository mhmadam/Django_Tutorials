from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='owner',null=True)
    title = models.CharField(max_length=200,null=True)
    caption = models.TextField(null=True,blank=True)
    video = models.FileField(upload_to='post/videos/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.video.delete()
        super().delete(*args, **kwargs)
