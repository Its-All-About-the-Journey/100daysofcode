import requests
import os
from datetime import *
from twilio.rest import Client

# Endpoint and API key for OpenWeatherMap.org
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = os.environ.get('OWM_API_KEY')

# Account SSID and token for Twilio
ACCOUNT_SSID = os.environ.get('TWILIO_ACCOUNT_SSID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

# My private phone number I used to sign up for Twilio
MY_NUM = os.environ.get('MY_PHONE_NUMBER')

# Parameters to pass into OWM API call
parameters = {
	'lat': 42.979008,
	'lon': -78.792274,
	'units': 'imperial',
	'exclude': 'current,minutely,daily',
	'appid': API_KEY

}

# Get the OWM response, convert to dictionary and get the hourly forecast for next 12 hours
response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
twelve_hour_weather = response.json()['hourly'][0:12]

# For each hour that will rain (Weather ID's < 600), convert the Unix time to local time (EST)
# and append it to the rainy_times list
rainy_times = []
for hour in twelve_hour_weather:
	if hour['weather'][0]['id'] < 600:
		unix = hour['dt']
		rainy_times.append(datetime.utcfromtimestamp(unix).strftime('%H:%M'))

# If it will rain in next 12 hours, SMS text my phone an alert containing the times it will rain
# Using the Twilio API
if len(rainy_times) > 0:
	print('It is going to rain at the following times: ')
	print(', '.join(rainy_times))
	client = Client(ACCOUNT_SSID, AUTH_TOKEN)
	message = client.messages.create(
		body=f"It is going to rain at the following times: {', '.join(rainy_times)}",
		from_='+12623203179',
		to=MY_NUM
	)
	print(message.status)
else:
	print("No Rain Today")
