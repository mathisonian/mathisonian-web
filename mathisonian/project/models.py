from django.db import models


class Project(models.Model):
    description = models.TextField()
    url = models.URLField()
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=300)
    img = models.ImageField(upload_to=".")
    created_at = models.DateTimeField(auto_now_add=True)
