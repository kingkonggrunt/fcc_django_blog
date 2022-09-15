from datetime import datetime

from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1_000_000)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)