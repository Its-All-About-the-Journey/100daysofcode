import requests

# Class to add users to Flight Club
class User:
	SHEETY_USERS_ENDPOINT = 'https://api.sheety.co/f647da55a331b83a0f820f6550cc9170/flightDeals/users'
	SHEETY_BEARER_TOKEN = 'Bearer SDKsndfkjnsSDKGJBS()W$(#%NSDFNSOI(#$Nsdjfns9'
	sheety_headers = {'Content-Type': 'application/json', 'Authorization': SHEETY_BEARER_TOKEN}

	# Initialize instance of class with name and email
	def __init__(self):
		self.user_data = {}

	# Function will post information to the Users google sheet using POST to Sheety API
	def add_user(self, fn, ln, email):
		first_name = fn
		last_name = ln
		email = email

		user_parameters = {
			'user': {
				'firstName': first_name,
				'lastName': last_name,
				'email': email
			}
		}
		response = requests.post(url=self.SHEETY_USERS_ENDPOINT, json=user_parameters, headers=self.sheety_headers)
		if response.raise_for_status() is not None:
			print(response.raise_for_status())
		if response.status_code == 200:
			print("You have been added to the club!")

	def get_users(self):
		self.user_data = requests.get(url=self.SHEETY_USERS_ENDPOINT, headers=self.sheety_headers).json()["users"]
		return self.user_data
