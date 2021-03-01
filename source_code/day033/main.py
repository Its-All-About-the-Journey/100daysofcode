import requests
from datetime import date, datetime
import math
import smtplib
import time

MY_LAT = 9.468736  # Your latitude
MY_LONG = 54.337214 # Your longitude

email = "emailviapython@gmail.com"

def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])    

    #Your position is within +5 or -5 degrees of the ISS position.
    if math.fabs(MY_LAT - iss_latitude) <= 5 and math.fabs(MY_LONG - iss_longitude) <= 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now >= sunset or hour_now <= sunrise:
        return True

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

while True:
    if check_position() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email,password="2TestPassPythonEmail")

            connection.sendmail(
                from_addr=email, 
                to_addrs=email, 
                msg=f"Subject:ISS Overhead\n\nLook up!"
                )
    time.sleep(60)