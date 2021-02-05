import os

import requests


try:
    API_KEY = os.environ["OWM_API_KEY"]

except KeyError:
    API_KEY = input("Enter your API key: ")

URL = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": 13.45,
    "lon": 138.41,
    "exclude": "current,minutely,daily"
}

if __name__ == "__main__":

    if API_KEY:
        params["appid"] = API_KEY

        response = requests.get(url=URL, params=params)
        response.raise_for_status()

        hour = 12
        data = response.json()["hourly"][:hour]

        while hour > 0:
            hour -= 1
            weather_id = data[hour]["weather"][0]["id"]

            if weather_id < 700:
                print(f"Bring an umbrella!")
                break

    else:
        print("No API KEY, exiting.")
