from django.db import models


class Project(models.Model):
    content = models.TextField()
    url = models.URLField()
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=300)
