from django.db import models
import requests
import json

TOKEN = 'FHO43SJ3VXJC6S3P2TRR'
baseURL = 'https://www.eventbriteapi.com/v3/'

class Query(models.Model):
    city = models.CharField(max_length=64, blank=True)
    region = models.CharField(max_length=64, blank=True)
    country = models.CharField(max_length=64, blank=True)
    categories = models.CharField(max_length=64)
    popular = models.BooleanField()
    
    def __init__(self):
        Query.categories = models.CharField(max_length=64, choices=self.get_categories())
    
    def get_categories(self):
        catURL = baseURL + 'categories/?token=' + TOKEN
        raw_result = requests.get(catURL)
        result = json.loads(raw_result.text)
        options_list = [(x['id'], x['name']) for x in result['categories']]
        return options_list
