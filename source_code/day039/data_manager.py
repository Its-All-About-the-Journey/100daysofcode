import os
import requests

BASE_URL = f"https://api.sheety.co/{os.environ['SHEETY_ID_FLIGHTS']}/flightDeals"
SHEETY_HEADERS = {
            "Authorization" : f"Bearer {os.environ['SHEETY_BEARER']}",
            "Content-Type" : "application/json"
        }

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.data = requests.get(url=f'{BASE_URL}/prices', headers=SHEETY_HEADERS).json()

    def sign_up():
        print("Welcome to Jake's Flight Club.\nWe find the best flight deals and email you.")
        f_name = input("What is your first name?\n")
        l_name = input("What is your last name?\n")
        while True:
            email = input("What is your email?\n")
            if input("Please enter your email again to confirm.\n") == email:
                break
            else: print("Emails do not match, please try again.\n")
            print("You're in the club!")

        user = {
            'user' : {
            'firstName' : f_name,
            'lastName' : l_name,
            'email' : email
            }
        }

        requests.post(url=f'{BASE_URL}/users', headers=SHEETY_HEADERS, json=user)
    
    def populate_iata(self, id, iata_update):
        requests.put(url=f'{BASE_URL}/{id}', headers=SHEETY_HEADERS, json=iata_update)
        self.data = requests.get(url=BASE_URL, headers=SHEETY_HEADERS).json()
    
    def get_emails(self):
        return requests.get(url=f'{BASE_URL}/users', headers=SHEETY_HEADERS).json()['users']