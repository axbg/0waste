from django.db import models

# Create your models here.
class FastTrack(models.Model):
    raw = models.TextField(blank=True, default="")
    annotated = models.TextField(blank=True, default="")
    location = models.TextField(blank=True, default="")

class ImpactMeasurement(models.Model):
    before_raw = models.TextField(blank=True, default="")
    after_raw = models.TextField(blank=True, default="")
    before_annotated = models.TextField(blank=True, default="")
    after_annotated = models.TextField(blank=True, default="")
    location = models.TextField(blank=True, default="")