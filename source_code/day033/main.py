from datetime import *
import os
import requests
import smtplib
import time

MY_LAT = 42.886027
MY_LONG = -78.877917
MY_EMAIL = os.environ.get('EMAIL')
MY_EMAIL_PASS = os.environ.get('EMAIL_PASS')
iss_lat = 0
iss_long = 0

def iss_is_nearby():
	global iss_lat, iss_long

	# Make call to ISS API
	response = requests.get(url='http://api.open-notify.org/iss-now.json')
	response.raise_for_status()  # If connection to API endpoint fails, will return the response code as an exception
	iss_data = response.json()

	# Retrieve ISS current latitude and longitude from the json object
	iss_lat = float(iss_data['iss_position']['latitude'])
	iss_long = float(iss_data['iss_position']['longitude'])

	# Determine if the ISS lat/long is close to my location by comparing positions
	if abs(MY_LAT - iss_lat) <= 5 and abs(MY_LONG - iss_long) <= 5:
		return True
	return False

def is_night():
	# Set parameters for call to sunrise-sunset API
	parameters = {
		'lat': MY_LAT,
		'lng': MY_LONG,
		'formatted': 0}

	# Make call to API, passing in parameters -> pull out sunrise/sunset times from json
	response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
	response.raise_for_status()
	sun_data = response.json()
	sunrise = sun_data['results']['sunrise']
	sunset = sun_data['results']['sunset']

	# Parse the sunrise and sunset hours (provided in UTC)
	sunrise_hour = int(sunrise.split('T')[1].split('+')[0].split(':')[0])
	sunset_hour = int(sunset.split('T')[1].split('+')[0].split(':')[0])

	# Get the current UTC hour
	utc_hour_now = datetime.utcnow().hour

	# Compare current time to sunrise/sunset to determine if it is night time
	if utc_hour_now >= sunset_hour or utc_hour_now <= sunrise_hour:
		return True
	return False

# Function will tell you which general direction to look to see the ISS
def return_direction():
	global iss_lat, iss_long
	if (MY_LONG - iss_long) > 1:
		ew = 'west'
	elif -1 <= (MY_LONG - iss_long) <= 1:
		ew = 'Up'
	elif (MY_LONG - iss_long) < -1:
		ew = 'east'
	if (MY_LAT - iss_lat) > 1:
		ns = 'South'
	elif -1 <= (MY_LAT - iss_lat) <= 1:
		ns = 'Straight'
	elif (MY_LAT - iss_lat) < -1:
		ns = 'North'
	return f'Look {ns}{ew}-ish'

while True:
	# Test to see if its night time and if the iss is near/overhead -> send email if both True
	if is_night and iss_is_nearby():
		with smtplib.SMTP('smtp.gmail.com') as connection:  # Use smtp server of whatever mail provider you're using
			connection.starttls()  # Secures our connection and encrypts our emails, should they be intercepted
			connection.login(user=MY_EMAIL, password=MY_EMAIL_PASS)
			connection.sendmail(from_addr=MY_EMAIL,
			                    to_addrs='gtarmstrong89@gmail.com',
			                    msg=f"Subject:LOOK UP!\n\nThe International Space Station can be seen in the sky from where"
			                        f" you are. {return_direction()}"
			                    )
	# Will pause 60s between checks
	time.sleep(60)
