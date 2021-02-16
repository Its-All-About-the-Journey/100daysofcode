# 100 Days of Code : Python
# Weather Checker
# Adam Pawlowski (@hypermanganate)

from requests import Session
from requests.exceptions import HTTPError
from app_config import API_KEY

session = Session()

params = {
    "lat": "42.985",
    "lon": "-78.878",
    "exclude": "current,mminutely,daily",
    "appid": API_KEY
}

endpoint = "https://api.openweathermap.org/data/2.5/onecall"

result = session.get(url=endpoint, params=params)

try:

    result.raise_for_status()

except HTTPError:

    print("Request failed.")

hourly_data = result.json()["hourly"]

rain = False
for hour in range(12):
    if hourly_data[hour]["weather"][0]["id"] < 700:
        rain = True

if rain:
    print("It may rain in the next 12 hours, grab an umbrella.")
else:
    print("Looks like a dry day ahead.")
