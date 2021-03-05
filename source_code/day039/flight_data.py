from datetime import datetime

class FlightData:

    def __init__(self, flight_info) -> None:
        self.via_city = ""
        try:
            flight_info["route"][2]
            dest_pos = 1
            return_pos = 2
            self.via_city = flight_info["route"][0]['cityTo']
        except IndexError:
            dest_pos = 0
            return_pos = 1
        self.origin = flight_info["route"][0]['cityFrom']
        self.origin_airport = flight_info["route"][0]['cityCodeFrom']
        self.destination = flight_info["route"][dest_pos]['cityTo']
        self.destination_airport = flight_info["route"][dest_pos]['cityCodeTo']
        self.date_from = str(datetime.fromtimestamp(flight_info['route'][0]['dTime']).strftime('%m/%d/%Y'))
        self.date_to = str(datetime.fromtimestamp(flight_info['route'][return_pos]['dTime']).strftime('%m/%d/%Y'))
        self.link_from = str(datetime.fromtimestamp(flight_info['route'][0]['dTime']).strftime('%Y-%m-%d'))
        self.link_to = str(datetime.fromtimestamp(flight_info['route'][return_pos]['dTime']).strftime('%Y-%m-%d'))
        self.price = flight_info['price']
        