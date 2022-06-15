from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import date, datetime
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    title_tag = models.CharField(max_length=255, default=title)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')
    summary = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=[(str(self.pk))])

    def total_likes(self):
        return self.likes.count()

