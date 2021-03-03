from requests import Session, HTTPError
from dateutil import relativedelta
import datetime
from pprint import pprint

from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, endpoint: str, token: str) -> None:
        self.endpoint = endpoint
        self.token = token
        self.session = Session()

    def get_iata_code(self, flight_city: str):

        headers = {
            "apikey": self.token
        }

        url = f"{self.endpoint}/locations/query"

        params = {
            "term": flight_city,
            "location_types": "city",
            "limit": 1,
        }

        results = self.session.get(
            url=url,
            headers=headers,
            params=params
        )

        try:

            results.raise_for_status()

        except HTTPError:

            print("Error retrieving IATA data")
            print(results.text)
            return False

        else:

            return results.json()['locations'][0]['code']

    def search_flight(
        self,
        origination_iata: str,
        destination_iata: str,
        stop_overs: int = 0,
         ):

        url = f"{self.endpoint}/v2/search"

        headers = {
            "apikey": self.token
        }

        date_from = datetime.datetime.today().strftime("%d/%m/%Y")
        date_to = datetime.datetime.today() + \
            relativedelta.relativedelta(months=6)
        date_to = date_to.strftime("%d/%m/%Y")

        params = {
            "fly_from": origination_iata,
            "fly_to": destination_iata,
            "dateFrom": date_from,
            "dateTo": date_to,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": stop_overs,
            "one_for_city": 1,
            "adults": 1,
            "curr": "USD",
        }

        response = self.session.get(
            url=url,
            headers=headers,
            params=params,
        )

        try:

            response.raise_for_status()

        except HTTPError:

            print("Error retrieving flight data.")
            print(response.text)

        else:

            if len(response.json()['data']) > 0:
                return FlightData(response.json()['data'][0], stop_overs)

            else:
                print(
                    f"No flights for {origination_iata} to " +
                    f"{destination_iata} with {stop_overs} stop overs!"
                     )
                return None
