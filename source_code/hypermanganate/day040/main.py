from requests.sessions import session
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
import json
import pprint

from requests import Session, HTTPError

config_file = json.load(fp=open("./app.cfg"))
config = config_file["app"]

SHEET_API_TOKEN = config["api"]["sheety"]["api_key"]
FLIGHT_SHEET_ENDPOINT = config["api"]["sheety"]["flight_endpoint"]
USERS_SHEET_ENDPOINT = config["api"]["sheety"]["users_endpoint"]

KIWI_API_TOKEN = config["api"]["kiwi"]["api_key"]
KIWI_ENDPOINT = config["api"]["kiwi"]["endpoint"]

FROM_MAIL = config["mail"]["Yahoo"]["address"]
TO_MAIL = config["mail"]["Live"]["address"]
SMART_HOST_ADDRESS = config["mail"]["Yahoo"]["smtp_host"]
SMART_HOST_PORT = config["mail"]["Yahoo"]["smtp_port"]
USERNAME = config["mail"]["Yahoo"]["address"]
PASSWROD = config["mail"]["Yahoo"]["pass"]


sheet = DataManager(FLIGHT_SHEET_ENDPOINT, SHEET_API_TOKEN)
flight_search = FlightSearch(KIWI_ENDPOINT, KIWI_API_TOKEN)
mailer = NotificationManager(
    from_mail=FROM_MAIL,
    to_mail=TO_MAIL,
    smart_host_address=SMART_HOST_ADDRESS,
    smart_host_port=SMART_HOST_PORT,
    username=USERNAME,
    password=PASSWROD
)

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

sheet_data = sheet.read()
#  List of Dict:
# {
#     "city": str,
#     "iataCode": str,
#     "lowestPrice" : int,
#     "id": int
# }


def update_flight_sheet():

    for record in sheet_data:
        if record['iataCode'] == '':
            print(f"Retrieving IATA Code for {record['city']}")
            iata_code = flight_search.get_iata_code(record['city'])
            print(f"Updating IATA Code to {iata_code}")
            sheet.update(
                record_id=record['id'],
                iataCode=iata_code
            )

        # Yes, you'll have to run it twice.
        else:

            candidate_flight = flight_search.search_flight(
                'BUF', record['iataCode']
                )

            if not candidate_flight:

                print(
                    "No flight found with 0 stopovers, " +
                    "attempting stopover search."
                    )
                candidate_flight = flight_search.search_flight(
                    'BUF', record['iataCode'], stop_overs=2
                     )

            if not candidate_flight:

                print("No flights with 1 stopover.")
                continue

            flight_price = candidate_flight.price

            print(f"{record['city']}: ${flight_price}")

            if flight_price < int(record['lowestPrice']):

                print(f"Flight to {record['city']} found cheaper!")
                if candidate_flight.via_city:
                    print(
                        f"Flight has 1" +
                        f" stop over, via {candidate_flight.via_city}."
                        )
                sheet.update(
                    record_id=record['id'],
                    lowestPrice=flight_price
                )

                mailer.send_mail(candidate_flight)


def signup_user():
    print("Welcome to the flight club.")
    print("Sign up for flight deals via e-mail.")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email1 = input("What is your e-mail address?\n")
    email2 = input("Please retype your e-mail for verification:\n")

    if email1 == email2:

        session = Session()

        payload = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email1
                }
        }

        headers = {
            "Authorization": f"Bearer {SHEET_API_TOKEN}"
        }

        results = session.post(
            url=USERS_SHEET_ENDPOINT,
            headers=headers,
            json=payload
            )

        try:

            results.raise_for_status()

        except HTTPError:

            print("Error updating user data.")
            print(results.text)

        else:

            print("Got it! You're in the club!")

    else:
        print("E-mail address didn't match. Try again.")


if __name__ == "__main__":
    ses = Session()
    headers = {
            "Authorization": f"Bearer {SHEET_API_TOKEN}"
        }
    # results = ses.get(USERS_SHEET_ENDPOINT, headers=headers)
    # print(results.json())
    # signup_user()
    update_flight_sheet()
