from django.db import models


class Query(models.Model):
    city = models.CharField(max_length=64, blank=True)
    region = models.CharField(max_length=64, blank=True)
    country = models.CharField(max_length=64, blank=True)
    categories = models.CharField(max_length=64, blank=True)
    popular = models.BooleanField(default=False)
    
