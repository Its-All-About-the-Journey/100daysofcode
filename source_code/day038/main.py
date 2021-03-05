import requests
from datetime import datetime
import os

APP_ID = os.environ['NUTRITIONIX_APP_ID']
API_KEY = os.environ['NUTRITIONIX_API_KEY']
SHEETY_BEARER = os.environ['SHEETY_BEARER']
SHEETY_URL = os.environ['SHEETY_URL']

nutritionix_headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "Content-Type" : "application/json"
}

sheety_headers = {
    "Authorization" : f"Bearer {SHEETY_BEARER}",
    "Content-Type" : "application/json"
}

nutritionix_params = {
    "query" : input("Tell me which exercises you did: ")
}

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = f"https://api.sheety.co/{SHEETY_URL}/myWorkouts/workouts"

response = requests.post(url=nutritionix_url, headers=nutritionix_headers, json=nutritionix_params)
exercises = response.json()["exercises"]
time_iso = datetime.now().time()
now_time = ((time_iso.hour + ((time_iso.minute + (time_iso.second / 60.0)) / 60.0)) / 24.0)

for exercise in exercises:
    data = {
        "workout" : {
            "date" : datetime.today().strftime('%d/%m/%Y'),
            "time" : datetime.now().strftime('%I:%M:%S %p'),
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

    requests.post(url=sheety_url, headers=sheety_headers, json=data)
