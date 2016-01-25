import requests
import json
import urllib.parse
import re

TOKEN = 'FHO43SJ3VXJC6S3P2TRR'
baseURL = 'https://www.eventbriteapi.com/v3/'

def get_categories():
    catURL = baseURL + 'categories/?token=' + TOKEN
    raw_result = requests.get(catURL)
    result = json.loads(raw_result.text)
    options_list = [(x['id'], x['name']) for x in result['categories']]
    options_list = sorted(options_list, key=lambda tup: tup[1])
    return options_list


def get_results(query):
    query_string = gen_query(query)
    eventURL = baseURL + 'events/search' + query_string
    authURL = eventURL + '&token=' + TOKEN
    raw_result = requests.get(authURL)
    result = json.loads(raw_result.text)
    return result


def validate_names(data):
    if re.search(r'^(?:[^\W\d_]| )+$', data):
        return True
    return False


def is_empty(data):
    print ('empty function called')
    return data is None or data.strip() == ''


def gen_query(query):
    query_string = '/?'
    if 'categories' in query:
        query_string += 'categories=' + ','.join(query['categories'])
        query_string += '&'
    query_string += '&'.join([x + '=' + query[x][0] for x in query if query[x][0]!='' and x!='categories' and x!='submit_flag'])
    query_string = query_string.replace('_', '.')
    if 'page' not in query:
        query_string += '&page=1'
    query_string = urllib.parse.quote_plus(query_string, safe='=&/?')
    return query_string
    