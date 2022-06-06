from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    title_tag = models.CharField(max_length=255, default=title)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

