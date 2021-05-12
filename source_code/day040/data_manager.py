import requests
import os

# This class is responsible for talking to the Google Sheet.
class DataManager:
	SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/f647da55a331b83a0f820f6550cc9170/flightDeals/prices'
	SHEETY_BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN')
	sheety_header = {'Content-Type': 'application/json', 'Authorization': SHEETY_BEARER_TOKEN}

	def __init__(self):
		self.sheet_data = {}

	# Will return everything in the "Flight Deals - Prices" google sheet using the Sheety API
	def get_sheet_data(self):
		response = requests.get(url=self.SHEETY_PRICES_ENDPOINT, headers=self.sheety_header)
		response.raise_for_status()
		self.sheet_data = response.json()["prices"]
		return self.sheet_data

	# Updates spreadsheet with IATA codes using PUT requests in Sheety
	def update_iata(self):
		for destination in self.sheet_data:
			# Create endpoint for PUT requests by combining normal endpoint with object ID
			sheety_put_endpoint = f"{self.SHEETY_PRICES_ENDPOINT}/{destination['id']}"
			# Create structured parameters variable containing new IATA code data
			sheety_parameters = {
				'price': {
					'iataCode': destination['iataCode']
				}
			}
			# PUT request to update each row with new IATA code found in parameters
			sheety_response = requests.put(url=sheety_put_endpoint, json=sheety_parameters, headers=self.sheety_header)
			sheety_response.raise_for_status()
