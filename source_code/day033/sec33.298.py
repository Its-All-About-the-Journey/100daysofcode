from datetime import datetime

import requests


URL = "https://api.sunrise-sunset.org/json"

PARAMETERS = {
    "lat": 37.411732,
    "lng": 121.932678,
    "formatted": 0
}

def request() -> dict:
    response = requests.get(url=URL, params=PARAMETERS)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    data = request()

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    print(f"Sunrise hour: {sunrise}")
    print(f"nSunset hour: {sunset}")
    print(f"Current hour: {datetime.now().hour}")