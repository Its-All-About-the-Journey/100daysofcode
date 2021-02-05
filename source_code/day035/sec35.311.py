import os

import requests


try:
    API_KEY = os.environ["OWM_API_KEY"]

except KeyError:
    API_KEY = input("Enter your API key: ")

URL = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": 37.411732,
    "lon": -121.932678,
}

if __name__ == "__main__":

    if API_KEY:
        params["appid"] = API_KEY

        response = requests.get(url=URL, params=params)
        response.raise_for_status()

        print(response.status_code)
    else:
        print("No API KEY, exiting.")
