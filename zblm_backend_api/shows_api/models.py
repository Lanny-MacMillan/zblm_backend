from django.db import models

# Create your models here.
class Show(models.Model):
    venue = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    coverPrice = models.IntegerField()
    other = models.TextField(blank=True)