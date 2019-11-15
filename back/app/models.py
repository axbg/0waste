from django.db import models

# Create your models here.
class FastTrack(models.Model):
    raw = models.TextField(blank=True, default="")
    annotated = models.TextField(blank=True, default="")
    location = models.TextField(blank=True, default="")