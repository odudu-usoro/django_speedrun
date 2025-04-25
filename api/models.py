from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=True)