#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from notification_manager import NotificationManager
from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager

ORIGIN = 'LHR'

data = DataManager()
flight_finder = FlightSearch()

if input("Would you like to sign up for flight deals? Y or N").upper() == 'Y':
    data.sign_up()

#Populate missing IATA Codes
for city in data.data['prices']:
    if city['iataCode'] == '':
        iata_code = flight_finder.iata_code_search(city['city'])
        iata_json = {
            "price" : {
                'iataCode' : iata_code
            }
        }
        data.populate_iata(city['id'], iata_json)

# Check for flights deals
for city in data.data['prices']:
    try:
        flight = flight_finder.check_for_deals(ORIGIN, city)
    except IndexError:
        print(f"No cheap flights available for {city['city']}")
    else:
        flight_data = FlightData(flight)
        text = NotificationManager()
        #text.send_message(flight_data)
        for email in data.get_emails():
            text.send_emails(email, flight_data)