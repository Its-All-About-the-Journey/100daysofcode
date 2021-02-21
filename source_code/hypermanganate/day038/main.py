# 100 Days of Code: Day 38
# Google Workout Spreadsheet
# Adam Pawlowski (@hypermanganate)

import json
import datetime
from requests import Session
from requests.models import HTTPError

config_file = json.load(fp=open("./app.cfg"))
config = config_file["app"]

NUTRITION_APP_ID = config["api"]["nutritionix"]["app_id"]
NUTRITION_APP_KEY = config["api"]["nutritionix"]["api_key"]
NUTIRTION_ENDPOINT = config["api"]["nutritionix"]["endpoint"]

SHEET_API_TOKEN = config["api"]["sheety"]["api_key"]
SHEET_ENDPOINT = config["api"]["sheety"]["endpoint"]

session = Session()


def get_nutrition_data(**kwargs):

    nutrition_headers = {
        "x-app-id": NUTRITION_APP_ID,
        "x-app-key": NUTRITION_APP_KEY,
        "x-remote-user-id": "0"
    }

    nutrition_payload = {
        "query": kwargs['exercise_query'],
        "gender": kwargs['gender'],
        "weight_kg": kwargs['weight_kg'],
        "height_cm": kwargs['height_cm'],
        "age": kwargs['age']
    }

    nutrition_results = session.post(
        url=NUTIRTION_ENDPOINT,
        json=nutrition_payload,
        headers=nutrition_headers
        )

    try:

        nutrition_results.raise_for_status()

    except HTTPError:

        print("Failed to get NutritionIX data")
        return False

    else:

        return nutrition_results.json()


def update_sheet(**kwargs):

    sheet_headers = {
        "Authorization": f"Bearer {SHEET_API_TOKEN}"
    }

    sheet_payload = {
        "workout": {
            "date": kwargs["date"],
            "time": kwargs["time"],
            "exercise": kwargs["exercise"],
            "duration" : kwargs["duration"],
            "calories": kwargs["calories"]
        }
    }

    sheet_results = session.post(
        SHEET_ENDPOINT,
        headers=sheet_headers,
        json=sheet_payload
        )

    try:

        sheet_results.raise_for_status()

    except HTTPError:

        print("Failed to update Google Sheet")
        return False

    else:

        return sheet_results.json()

# Main


query = input("What exercises did you do today? ")

nutrition_request = {
    "exercise_query": query,
    "gender": "male",
    "weight_kg": 106.59,
    "height_cm": 185.42,
    "age": 34
}

nutrition_data = get_nutrition_data(**nutrition_request)

if nutrition_data:
    for exercise in nutrition_data["exercises"]:
        print("Detected exercise:")
        print(exercise['name'])
        print(
            f"Exercise lasted for {exercise['duration_min']} minutes and " +
            f"burned {exercise['nf_calories']} calories (est)."
        )

        exercise_request = {
            "date": datetime.datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.datetime.today().strftime("%H:%M:%S"),
            "exercise": exercise['name'],
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }

        sheet_results = update_sheet(**exercise_request)

        if sheet_results:
            print("Got it !")
            print(
                f"Added record #{int(sheet_results['workout']['id']) - 1} " +
                "to your fitness log!"
                )
