from twilio.rest import Client
import os
import smtplib

# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    # Account SSID and token for Twilio
    TWILIO_SSID = 'ACfa787da7b1ebbc946927b08deaac798b'
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    # Private phone number I used to sign up for Twilio
    MY_NUM = os.environ.get('MY_PHONE_NUMBER')
    # My email credentials
    MY_EMAIL = os.environ.get('EMAIL')
    MY_EMAIL_PASS = os.environ.get('EMAIL_PASS')

    def __init__(self, sheet_data, flight_data):
        self.sheet_data = sheet_data
        self.flight_data = flight_data
        self.message = ''

    # Function will compare the flight prices to the desired price in the spreadsheet and notify me via SMS text if
    # lower price is found -> also emails all users the deals
    # Adds layover information to message if flight has layovers
    def compare_prices_and_notify(self, user_data, has_layovers=False):
        for flight in self.flight_data:
            for row in self.sheet_data:
                if flight["arrival_city"] == row['city'] and flight['price'] < row['lowestPrice']:
                    found_cheaper_flight = True
                    self.message = f'Low price alert! Only ${flight["price"]} to fly from {flight["departure_city"]} ' \
                                  f'({flight["departure_airport_code"]}) to {flight["arrival_city"]} ' \
                                  f'({flight["arrival_airport_code"]}), from {flight["departure_date"]} to ' \
                                  f'{flight["return_date"]}.'

                    # If the flight has layovers, add additional information to the message
                    if has_layovers:
                        self.message += f' This flight has {flight["num_outbound_layovers"]} outbound layover(s) in ' \
                                       f'{" and ".join(flight["outbound_layover_cities"])} and ' \
                                       f'{flight["num_return_layovers"]} return layover(s) in ' \
                                       f'{" and ".join(flight["return_layover_cities"])}.'

                    # Create and send the message via Twilio
                    client = Client(self.TWILIO_SSID, self.TWILIO_AUTH_TOKEN)
                    client.messages.create(body=self.message, from_='+12623203179', to=self.MY_NUM)

                    # Send email to all users containing the message
                    for user in user_data:
                        user_email = user['email']
                        user_fn = user['firstName']
                        user_ln = user['lastName']
                        user_full_name = f'{user_fn} {user_ln}'

                        with smtplib.SMTP('smtp.gmail.com') as connection:
                            connection.starttls()
                            connection.login(user=self.MY_EMAIL, password=self.MY_EMAIL_PASS)
                            connection.sendmail(from_addr=self.MY_EMAIL,
                                                to_addrs=user_email,
                                                msg=f"Subject:{user_full_name}, we have a flight deal just for you!\n\n"
                                                    f"{self.message}"
                                                )
