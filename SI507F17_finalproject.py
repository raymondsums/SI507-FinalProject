import requests
import geocoder
import oauth2
import json
import random
import psycopg2
import os
import sys
import psycopg2.extras
from datetime import datetime
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode
from config import db_name, db_user
from secret_data import CLIENT_ID, CLIENT_SECRET
# from flask import Flask, render_template
# from flask_script import Manager

def time():
    now = datetime.now()
    return now

def search_term():
    DEFAULT_TERM = input('What do you want to search for: ')
    if type(DEFAULT_TERM) == None:
        DEFAULT_TERM = 'Restaurants'
        return DEFAULT_TERM
    else:
        return DEFAULT_TERM

def has_cache_expired(timestamp_str, expire_in_days=7):
    cache_timestamp = datetime.strptime(timestamp_str, DATETIME_FORMAT)
    delta = time() - cache_timestamp
    delta_in_days = delta.days

def set_in_data_cache(identifier, data, expire_in_days=7):
    identifier = identifier.upper()
    CACHE_DICTION[identifier] = {
        'values': data,
        'timestamp' : datetime.now().strftime(DATETIME_FORMAT),
        'expire_in_days': expire_in_days
    }

    with open(CACHE_FNAME,'w') as cache_file:
        cache_file.write(json.dumps(CACHE_DICTION))

def get_from_cache(identifier,dictionary):
    identifier = identifier.upper()
    if identifier in dictionary:
        data_assoc_dict = dictionary[identifier]
        if has_cache_expired(data_assoc_dict['timestamp'],data_assoc_dict['expire_in_days']):
            print("Cache has expired for {}".format(identifier))
            del dictionary[identifier]
            data = None
        else:
            data = dictionary[identifier]['values']
    else:
        data = None
    return data

def user_location():
    user_location = input('Where is your location: ')
    if len(user_location) == 0:
        g = geocoder.ip('me')
        user_location = g.json['address']
        return user_location
    else:
        return user_location

def obtain_bearer_token(host, path):
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token

def request(host, path, bearer_token, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    response = requests.request('GET', url, headers=headers, params=url_params)
    return response.json()

def get_search_data(bearer_token, term= search_term(), location=user_location()):
    ident = term
    data = get_from_cache(ident, CACHE_DICTION)
    if data:
        return data
    else:
        url_params = {
            'term': term.replace(' ', '+'),
            'location': location.replace(' ', '+'),
            'limit': 50
        }
        data = (request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params))['businesses']
        set_in_data_cache(ident, data)
    return data

def get_business_data(bearer_token, business_id):
    ident = business_id
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path, bearer_token)

def rng():
    return random.randint(1,len(business_list)-1)

REQUEST_TOKEN_URL = 'https://api.yelp.com/oauth2/token'
baseurl = "https://api.yelp.com/v3/businesses/search"

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

bearer_token = obtain_bearer_token(API_HOST,TOKEN_PATH)

CACHE_FNAME = "cache_contents.json"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

#for caching purposes
try:
    with open(CACHE_FNAME, 'r') as cache_file:
        cache_json = cache_file.read()
        CACHE_DICTION = json.loads(cache_json)
except:
    CACHE_DICTION = {}

business_list = []
business_dict = {}
for i in get_search_data(bearer_token):
    business_dict['ID'] = i['id']
    business_dict['Name'] = i['name']
    business_list.append(i['name'])
    business_dict['Review_Count'] = i['review_count']
    business_dict['Rating'] = i['rating']
    try:
       business_dict['Price'] = i['price']
    except:
       business_dict['Price'] = 'No Price Info'
    business_dict['Address'] = i['location']['address1']
    try:
    	business_dict['City'] = i['city']
    except:
    	business_dict['City'] = 'No City Info'
    try:
       business_dict['Hours'] = (get_business_data(bearer_token,i['id']))['hours']
    except:
       business_dict['Hours'] = 'No Operating Hours Info'

db_connection = None
db_cursor = None

def load_cache():
	global CACHE_DICTION
	try:
		cache_file = open(CACHE_FNAME,'r')
		cache_contents = cache_file.read()
		CACHE_DICTION = json.loads(cache_contents)
		cache_file.close()
	except:
		CACHE_DICTION = {}


try:
 	conn = psycopg2.connect("dbname='{0}' user='{1}'".format(db_name, db_user))
 	print("Success connecting to database")
except:
 	print("Unable to connect to database. Check server and credentials.")
 	sys.exit(1)

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("DROP TABLE IF EXISTS Restaurant_Info")
cur.execute("DROP TABLE IF EXISTS Restaurant_Hours")

cur.execute("CREATE TABLE IF NOT EXISTS Restaurant_Info(ID SERIAL PRIMARY KEY, Yelp_ID VARCHAR(64), Name VARCHAR(64), Review_Count INTEGER, Rating INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS Restaurant_Hours(ID SERIAL PRIMARY KEY, Day INTEGER, Hours INTEGER)")
conn.commit()
print('Setup database complete')

# def insert(conn, cur, table, data_dict):
# 	column_names = data_dict.keys()
# 	print(column_names)
#     conn.commit()

rng_1 = rng()
rng_2 = rng()-1
rng_3 = rng()-2
rng_4 = rng()-3
rng_5 = rng()-4

choice_1 = business_list[rng_1]
business_list.pop(rng_1)
choice_2 = business_list[rng_2]
business_list.pop(rng_2)
choice_3 = business_list[rng_3]
business_list.pop(rng_3)
choice_4 = business_list[rng_4]
business_list.pop(rng_4)
choice_5 = business_list[rng_5]
business_list.pop(rng_5)

print("1.",choice_1,
    "2.",choice_2,
    "3.", choice_3,
    "4.", choice_4,
    "5.", choice_5)

with open('cache_contents.json') as f:
    response_json = f.read()
    data = json.loads(response_json)
    print(data['RESTAURANTS']['values'][0])

# app = Flask(__name__)

# @app.route('/')
# def restaurants():
#     with open('cache_contents.json') as f:
#         response_json = f.read()
#         data = json.loads(response_json)

#     return data['RESTAURANTS']['values']


# if __name__ == '__main__':
#     app.run(use_reloader=True)

# Referred to Yelp Fusion API Github Page at https://yelp.com/developers
# Referred to hartleybrody/fb-messenger-bot on GitHub
