from django.db import models
from django.db.models import Model


class Video(models.Model):
    title = models.URLField(max_length=200)

# Create your models here.
