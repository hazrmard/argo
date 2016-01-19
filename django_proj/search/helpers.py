import requests
import json
import urllib.parse

TOKEN = 'FHO43SJ3VXJC6S3P2TRR'
baseURL = 'https://www.eventbriteapi.com/v3/'

def get_categories():
    catURL = baseURL + 'categories/?token=' + TOKEN
    raw_result = requests.get(catURL)
    result = json.loads(raw_result.text)
    options_list = [(x['id'], x['name']) for x in result['categories']]
    return options_list

def get_results(query):
    query_string = '&'.join([x + '=' + query[x] for x in query if query[x]!=''])
    query_string = query_string.replace('_', '.')
    query_string = urllib.parse.quote_plus(query_string, safe='=&')
    eventURL = baseURL + 'events/search/?token=' + TOKEN + '&' + query_string
    print('URL is: ' + eventURL)
    raw_result = requests.get(eventURL)
    result = json.loads(raw_result.text)
    print(len(result['events']))
    return result