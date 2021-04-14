from twilio.rest import Client
import os

# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    # Account SSID and token for Twilio
    TWILIO_SSID = 'ACfa787da7b1ebbc946927b08deaac798b'
    TWILIO_AUTH_TOKEN = 'd45c15b0cb24d676cda618e762b17887'
    # Private phone number I used to sign up for Twilio
    MY_NUM = os.environ.get('MY_PHONE_NUMBER')

    def __init__(self, sheet_data, flight_data):
        self.sheet_data = sheet_data
        self.flight_data = flight_data

    # Function will compare the flight prices to the desired price in the spreadsheet and notify user via SMS text if
    # lower price is found
    def compare_prices_and_notify(self):
        found_cheaper_flight = False

        for flight in self.flight_data:
            for row in self.sheet_data:
                if flight["arrival_city"] == row['city'] and flight['price'] < row['lowestPrice']:
                    found_cheaper_flight = True
                    sms_message = f'Low price alert! Only ${flight["price"]} to fly from {flight["departure_city"]} ' \
                                  f'({flight["departure_airport_code"]}) to {flight["arrival_city"]} ' \
                                  f'({flight["arrival_airport_code"]}), from {flight["departure_date"]} to ' \
                                  f'{flight["return_date"]}.'
                    client = Client(self.TWILIO_SSID, self.TWILIO_AUTH_TOKEN)
                    client.messages.create(body=sms_message, from_='+12623203179', to=self.MY_NUM)
                # Notify user in console if a cheaper flight isn't found
                if not found_cheaper_flight:
                    print("No flights below designated price points have been found.")
