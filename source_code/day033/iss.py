
import requests
from datetime import datetime


parameters = {
    "lat": 37.411732,
    "lng": 121.932678,
    "formatted": 0
}


def is_iss_overhead() -> bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    lat_diff = abs(iss_latitude - parameters["lat"])
    lng_diff = abs(iss_longitude - parameters["lng"])

    return lat_diff < 5 and lng_diff < 5


def is_night() -> bool:
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    return hour_now >= sunset or hour_now <= sunrise


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if __name__ == "__main__":

    if is_iss_overhead() and is_night():
        # TODO: send email
        print("Look at sky!")