import requests
from datetime import datetime, timedelta

# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    LOCATIONS_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'  # Endpoint to get IATA codes
    SEARCH_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'  # Flight search endpoint
    TEQUILA_API_KEY = '3fCExRFdmUfMQGZSW0CXZbttPnfKw8gx'
    header = {'apikey': TEQUILA_API_KEY, 'Content-Encoding': 'gzip'}
    departure_city_iata = 'LON'  # (Buffalo = IAG, London = LON, New York City = NYC )
    tomorrows_date = (datetime.now() + timedelta(days=1)).strftime('%d/%m/%Y')  # Formatted as required by API
    six_months_date = (datetime.now() + timedelta(days=181)).strftime('%d/%m/%Y')  # Formatted as required by API

    # Pass a city destination to the function and it returns an individual IATA code (used for searching for flights)
    def return_iata(self, destination):
        locations_parameters = {
            'apikey': self.TEQUILA_API_KEY,
            'term': destination,
            'location_types': 'city'
        }
        locations_response = requests.get(url=self.LOCATIONS_ENDPOINT, params=locations_parameters,
                                          headers=self.header)
        locations_response.raise_for_status()
        iata_code = locations_response.json()['locations'][0]['code']
        return iata_code

    # Function returns the cheapest flight for each destination within the defined parameters
    def get_flights(self, destinations_iata):
        search_parameters = {
            'fly_from': self.departure_city_iata,
            'fly_to': destinations_iata,
            'date_from': self.tomorrows_date,
            'date_to': self.six_months_date,
            'nights_in_dst_from': 7,  # Minimum number of nights spent at destination
            'nights_in_dst_to': 28,  # Maximum number of nights spent at destination
            'flight_type': 'round',
            'one_for_city': 1,  # Return 1 result for each destination city
            'adults': 1,
            'adult_hold_bag': '1',
            'adult_hand_bag': '1',
            'curr': 'USD',  # USD for dollars
            'max_stopovers': 0,
            'vehicle_type': 'aircraft',
        }
        search_response = requests.get(url=self.SEARCH_ENDPOINT, params=search_parameters, headers=self.header)
        search_response.raise_for_status()
        return search_response.json()["data"]
