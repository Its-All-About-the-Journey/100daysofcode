import requests
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = (response.json())

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]


response = requests.get(url="https://api.sunrise-sunset.org/json", params={'lat': latitude, 'lng' : longitude, 'formatted' : 0})

sunrise = response.json()['results']['sunrise'].split('T')[1].split(':')[0]
sunset = response.json()['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)


