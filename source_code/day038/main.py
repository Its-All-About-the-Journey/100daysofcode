# Day038 Exercise Tracking Application (100DaysOfCode)
# Author: Grant Armstrong
# 4/2/2021

import requests
from datetime import datetime
import os

# Nutritionix API key, App ID and endpoint for API
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# Endpoint for Sheety API for "My Workouts" Google Sheet and Sheety Bearer Token for Auth
SHEETY_WORKOUTS_ENDPOINT = os.environ.get('SHEETY_WORKOUTS_ENDPOINT')
SHEETY_BEARER_TOKEN = os.environ.get('SHEETY_BEARER_TOKEN')

# User details
USER_GENDER = 'male'
USER_WEIGHT_KG = 97.5
USER_HEIGHT_CM = 177.8
USER_AGE = 31

exercise_input = input("Enter what exercises you did and how much: ")

# Headers passed to Nutritionix API
exercise_headers = {
	'x-app-id': NUTRITIONIX_APP_ID,
	'x-app-key': NUTRITIONIX_API_KEY,
	'x-remote-user-id': '0'
}

# Parameters passed to Nutritionix API
exercise_parameters = {
	'query': exercise_input,
	'gender': USER_GENDER,
	'weight_kg': USER_WEIGHT_KG,
	'height_cm': USER_HEIGHT_CM,
	'age': USER_AGE
}

# Post info to API and retrieve the exercises portion of the response
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_parameters, headers=exercise_headers)
workout_info = response.json()['exercises']

# Documentation says to set 'Content-Type'... Also use Bearer token authentication
sheety_headers = {
	'Content-Type': 'application/json',
	'Authorization': f'Bearer {SHEETY_BEARER_TOKEN}'
}

# Loop through exercises and use Sheety to post the exercise name, duration and # of calories burned to spreadsheet
for exercise in workout_info:
	# Be sure you use lowercase for each key or it won't work, even if the sheet uses uppercase
	print(exercise['user_input'].title(), exercise['duration_min'], exercise['nf_calories'])
	sheety_parameters = {
		'workout': {
			'date': datetime.now().strftime('%m/%d/%Y'),
			'time': datetime.now().strftime('%H:%M:%S'),
			'exercise': exercise['user_input'].title(),
			'duration': exercise['duration_min'],
			'calories': exercise['nf_calories']
		}
	}

	sheety_response = requests.post(url=SHEETY_WORKOUTS_ENDPOINT, json=sheety_parameters, headers=sheety_headers)

	# Print the response to confirm all details posted correctly
	print(sheety_response.text)
