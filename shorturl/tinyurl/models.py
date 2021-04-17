from django.db import models

# Create your models here.


class ShortUrlModel(models.Model):
    hash = models.CharField(max_length=32)
    url = models.TextField()

