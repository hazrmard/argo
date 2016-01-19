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
    query_string = '/?' + '&'.join([x + '=' + query[x] for x in query if query[x]!=''])
    query_string = query_string.replace('_', '.')
    query_string = urllib.parse.quote_plus(query_string, safe='=&/?')
    print(query_string)
    eventURL = baseURL + 'events/search' + query_string
    authURL = eventURL + '&token=' + TOKEN
    raw_result = requests.get(authURL)
    result = json.loads(raw_result.text)
    return result, query_string