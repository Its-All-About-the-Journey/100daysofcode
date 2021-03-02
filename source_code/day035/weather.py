import requests
from requests import api
from twilio.rest import Client
import datetime
import os

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

api_key = '611bd1269ba830fbdee1e7238be58c3c'
latitude = 44.992423
longitude = -93.286770

parameters = {
    'lat' : latitude,
    'lon' : longitude,
    'exclude': 'current,minutely,daily,alerts',
    'appid' : api_key
}

will_rain = False

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

for hour in weather_slice:
    condition = hour['weather'][0]['id']
    if condition < 700:
        will_rain = True
        time = datetime.datetime.utcfromtimestamp(hour['dt'])
        message = f"It will start raining at {time.strftime('%I:%M:%S %p')}"
        break

if will_rain:
    message = client.messages \
                    .create(
                        body=message,
                        from_='+19522434466',
                        to='+19522398656'
                    )
    print(message.status)
