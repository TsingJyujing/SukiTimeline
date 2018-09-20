from __future__ import unicode_literals
from django.db import models


class EventModel(models.Model):
    id = models.AutoField(primary_key=True)
    tick = models.FloatField(unique=True)
    title = models.TextField(max_length=30)
    comment = models.TextField(max_length=1000)
    image_hash = models.TextField(max_length=128)