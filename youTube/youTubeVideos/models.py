from django.db import models
from django.db.models import Model
from embed_video.fields import EmbedVideoField
from django.db import models


class Video(models.Model):
    video = EmbedVideoField(max_length=200, default=0)
    title = models.CharField(max_length=50, default=0)

# Create your models here.
