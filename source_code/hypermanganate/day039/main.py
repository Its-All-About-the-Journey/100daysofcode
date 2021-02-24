from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
import json

config_file = json.load(fp=open("./app.cfg"))
config = config_file["app"]

SHEET_API_TOKEN = config["api"]["sheety"]["api_key"]
SHEET_ENDPOINT = config["api"]["sheety"]["endpoint"]

KIWI_API_TOKEN = config["api"]["kiwi"]["api_key"]
KIWI_ENDPOINT = config["api"]["kiwi"]["endpoint"]

FROM_MAIL = config["mail"]["Yahoo"]["address"]
TO_MAIL = config["mail"]["Live"]["address"]
SMART_HOST_ADDRESS = config["mail"]["Yahoo"]["smtp_host"]
SMART_HOST_PORT = config["mail"]["Yahoo"]["smtp_port"]
USERNAME = config["mail"]["Yahoo"]["address"]
PASSWROD = config["mail"]["Yahoo"]["pass"]


sheet = DataManager(SHEET_ENDPOINT, SHEET_API_TOKEN)
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

        flight_price = candidate_flight.price

        print(f"{record['city']}: ${flight_price}")

        if flight_price < int(record['lowestPrice']):

            print(f"Flight to {record['city']} found cheaper!")
            sheet.update(
                record_id=record['id'],
                lowestPrice=flight_price
            )

            mailer.send_mail(candidate_flight)
