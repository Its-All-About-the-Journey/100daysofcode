import os
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

BASE_URL = 'https://tequila-api.kiwi.com'
HEADERS = {
            'accept' : 'application/json',
            'apikey' : os.environ['TEQUILA_API_KEY']
        }

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def check_for_deals(self, origin_city, data):
        deal_params = {
            'fly_from' : origin_city,
            'fly_to' : data['iataCode'],
            'date_from' : datetime.now().strftime('%m/%d/%Y'),
            'date_to' : (datetime.today() + relativedelta(month=+6)).strftime('%m/%d/%Y'),
            'price_to': data['lowestPrice'],
            'nights_in_dst_from' : 7,
            'nights_in_dst_to' : 28,
            'flight_type' : 'round',
            'max_stopovers' : 0,
            'curr' : 'USD'
        }
        try:
            return requests.get(url=f"{BASE_URL}/search", headers=HEADERS, params=deal_params).json()['data'][0]
        except IndexError:
            deal_params['max_stopovers'] = 2
            return requests.get(url=f"{BASE_URL}/search", headers=HEADERS, params=deal_params).json()['data'][0]

    def iata_code_search(self, city):
        location_params = {
            'term' : city,
            'locale' : 'en-US',
            'location_types' : 'airport',
            'limit' : '1',
            'active_only' : 'true'
        }
        return requests.get(url=f"{BASE_URL}/locations/query", headers=HEADERS, params=location_params).json()['locations'][0]['code']