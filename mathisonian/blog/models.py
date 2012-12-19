from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User)
    content = models.TextField()
    title = models.CharField(max_length=200)


class Comment(models.Model):
    owner = models.ForeignKey(User)
    content = models.TextField()
    post = models.ForeignKey(Post)
