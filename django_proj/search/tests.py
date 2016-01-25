from django.test import SimpleTestCase, Client
from .helpers import *
import requests

class SearchAppCases(SimpleTestCase):        
    def test_name_check(self):
        self.assertTrue(validate_names('Los Angeles'))
        self.assertTrue(validate_names('Canada'))
        self.assertFalse(validate_names('C@lifornia'))
        self.assertFalse(validate_names('U.S.A'))
        self.assertFalse(validate_names('N0rth Korea is Best Korea'))
    
    def test_empty_check(self):
        self.assertTrue(is_empty(None))
        self.assertTrue(is_empty('     '))
        self.assertFalse(is_empty('Nashville'))
    
    def test_working_urls(self):
        q = gen_query({'venue_city':'Nashville', 'venue_region': 'TN', 'categories':['103','110']})
        categories_URL = baseURL + 'categories/?token=' + TOKEN
        events_URL = baseURL + 'events/search' + q + '&token=' + TOKEN
        categories_response = requests.get(categories_URL)
        events_response = requests.get(events_URL)
        self.assertEqual(categories_response.status_code, 200)
        self.assertEqual(events_response.status_code, 200)
    
    def test_client(self):
        c = Client()
        q= gen_query({'venue_city':'Nashville', 'venue_region': 'TN', 'categories':['103','110']})
        self.assertEqual(c.get('/').status_code, 200)
        self.assertEqual(c.get(q).status_code, 200)
        
