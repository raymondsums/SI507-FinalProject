import requests
import geocoder
import oauth2
from datetime import datetime
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

def time():
    now = datetime.now()
    return now

def user_location():
    try:
        user_location = input('Where are you at: ')
    except:
        g = geocoder.ip('me')
        user_location = g.json['address']
        user_coordinates = g.latlng
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
    print(bearer_token)
    return bearer_token

def request(host, path, bearer_token, url_params=None):
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % bearer_token,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()

def search(bearer_token, term, location):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': 50
    }
    return request(API_HOST, SEARCH_PATH, bearer_token, url_params=url_params)

def get_business(bearer_token, business_id):
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path, bearer_token)

REQUEST_TOKEN_URL = 'https://api.yelp.com/oauth2/token'
baseurl = "https://api.yelp.com/v3/businesses/search"

CLIENT_ID = 'U6yNNGOPhxvAmadBOcVyVw'
CLIENT_SECRET = '9XWoYvtUTfBvOXYmNdjAajfOPzIw5wCrZojtZubRuB3jYzSJxaK6tocuHAKSvQo1'

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

DEFAULT_TERM = input('Enter search term: ')

bearer_token = obtain_bearer_token(API_HOST,TOKEN_PATH)
print(request(API_HOST,SEARCH_PATH,obtain_bearer_token(API_HOST,TOKEN_PATH)))
print(search(bearer_token,DEFAULT_TERM,user_location())['businesses'][0])
#print(get_business(bearer_token,(search(bearer_token,DEFAULT_TERM,user_location())['businesses'][0]['id'])))

# Referred to Yelp Fusion API Github Page at https://yelp.com/developers
