import requests
from twilio.rest import Client
import os
from email import message
import smtplib

ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
EMAIL_ACCOUNT = os.environ['EMAIL_ACCOUNT']
EMAIL_PASS = os.environ['EMAIL_PASS']
PHONE = os.environ['CELL_NUMBER']
CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def send_message(text_message_details):
        text_message = f"Low price alert! Only ${text_message_details.price} to fly from {text_message_details.origin}-{text_message_details.origin_airport} to {text_message_details.destination}-{text_message_details.destination_airport}, from {text_message_details.date_from} to {text_message_details.date_to}"
        if text_message_details.via_city != "":
            text_message += f"\n\nFlight has 1 stop over, via {text_message_details.via_city}"
        message = CLIENT.messages \
                    .create(
                        body=text_message,
                        from_=TWILIO_NUMBER,
                        to=PHONE
                    )

    def send_emails(email, text_message_details):
        to_address = email['email']
        link = f"https://www.google.com/flights?hl=en#flt={text_message_details.origin_airport}.{text_message_details.destination_airport}.{text_message_details.link_from}*{text_message_details.destination_airport}.{text_message_details.origin_airport}.{text_message_details.link_to}"
        text_message = f"Low price alert! Only ${text_message_details.price} to fly from {text_message_details.origin}-{text_message_details.origin_airport} to {text_message_details.destination}-{text_message_details.destination_airport}, from {text_message_details.date_from} to {text_message_details.date_to}\n\nBook here: {link}"
        if text_message_details.via_city != "":
            text_message += f"\n\nFlight has 1 stop over, via {text_message_details.via_city}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL_ACCOUNT,password=EMAIL_PASS)
                connection.sendmail(
                    from_addr=EMAIL_ACCOUNT, 
                    to_addrs=to_address,
                    msg=f"Subject:Flight Deal!\n\n{text_message}"
                    )