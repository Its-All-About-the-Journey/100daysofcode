# 100 Days of Code: Python
# Day 33
# API Examples
# Adam Pawlowski (@hypermanganate)

from time import sleep
from requests.models import HTTPError
from requests.sessions import Session
import datetime
import smtplib
import json

iss_api_endpoint = 'http://api.open-notify.org/iss-now.json'
suntime_api_endpoint = 'http://api.sunrise-sunset.org/json' + \
    '?lat={lat_float}&lng={lon_float}'
suntime_api_endpoint_raw = 'http://api.sunrise-sunset.org/json'

email_account = json.load(open('./email.cfg', 'r'))

my_api = Session()

MY_LAT = 43.003700  # Your latitude
MY_LONG = -78.857980  # Your longitude


def send_mail(
    message_body: str,
    to_address: str = email_account['Live']['address'],
    subject: str = "Motivational Quote"
     ):
    """
    Send email with a given subject, recipient, and message body.
    """

    connection = smtplib.SMTP(
        email_account['Yahoo']['smtp_host'],
        port=email_account['Yahoo']['smtp_port']
        )

    # Enable to debug SMTP transaction
    # connection.set_debuglevel(1)

    connection.starttls()

    connection.login(
        user=email_account['Yahoo']['address'],
        password=email_account['Yahoo']['pass']
        )

    message = f"From: {email_account['Yahoo']['address']}\n" + \
              f"To: {to_address}\n" + \
              f"Subject: {subject}\n\n" + \
              message_body

    connection.sendmail(
        from_addr=email_account['Yahoo']['address'],
        to_addrs=to_address,
        msg=message
        )

    connection.close()


def get_sun_times(coords: tuple):
    """
    Return sunrise/sunset data for a given lat/long
    """

    lat_float = coords[0]
    lon_float = coords[1]

    params = {
        "lat": lat_float,
        "lng": lon_float,
        "formatted": 0
    }

    # results = my_api.get(
    #    suntime_api_endpoint.format(
    #       lat_float=lat_float,
    #       lon_float=lon_float
    #     )
    #  )
    results = my_api.get(suntime_api_endpoint_raw, params=params)

    try:

        results.raise_for_status

    except HTTPError:
        pass

    if not results.json()['status'] == "OK":
        print("Soemthing went wrong getting sun times.")
        return False

    return results.json()['results']


def get_iss_location():
    """
    Get the lat/long of the ISS
    """

    results = my_api.get(iss_api_endpoint)

    try:

        results.raise_for_status()
    except HTTPError:

        print("Something went wrong:")
        print(f"Code: {results.status_code}")
        print(f"Message: {results.text}")
        return False

    results_json = results.json()

    if results_json['message'] != 'success':
        print("API fault, data not avaialble.")
        return False

    else:
        iss_position = (
            float(results_json['iss_position']['latitude']),
            float(results_json['iss_position']['longitude'])
            )

        return iss_position


def notifier():

    iss_position = get_iss_location()
    print(f"The ISS is located at : {iss_position}")
    sun_times_json = get_sun_times((MY_LAT, MY_LONG))

    print(
        "The sunset time, where you are now, is" +
        f" {sun_times_json['sunset']}"
    )

    # Compute if we're nearby.

    if (MY_LAT - 5 <= iss_position[0] <= MY_LAT + 5) \
            and (MY_LONG - 5 <= iss_position[1] <= MY_LONG + 5):

        # Your position is within +5 or -5 degrees of the ISS position.
        print("The ISS may be overhead!")

        my_sunset = datetime.datetime.strptime(
            sun_times_json['sunset'],
            '%Y-%m-%dT%H:%M:%S%z'
            )

        if my_sunset.hour <= datetime.datetime.utcnow().hour:

            print("It might be visible! Sending notification!")
            send_mail(
                message_body="The ISS is near your position now ... look up!",
                subject="ISS Notification"
            )

        else:

            print("It's not dark enough to see it.")

    else:

        print("The ISS isn't nearby. We'll check again soon.")

# main


while True:

    notifier()
    print("Sleeping...")
    sleep(60)
    exit()
