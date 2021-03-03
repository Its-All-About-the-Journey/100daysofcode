class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight_data: dict, stop_overs: int) -> None:

        # General Flight Data

        self.airport_from = flight_data.get('flyFrom')
        self.city_from = flight_data.get('cityFrom')
        self.airport_to = flight_data.get('flyTo')
        self.city_to = flight_data.get('cityTo')
        # This is a list but perhaps per leg?
        # Not really useful data
        self.route = flight_data.get('routes')

        self.departure_time = flight_data['route'][0].get('local_departure')
        self.arrival_time = flight_data['route'][-1].get('local_arrival')

        # This is a list
        self.airlines = flight_data.get('airlines')

        # Destination Data
        self.nights_in_destination = flight_data.get('nightsInDest', None)

        # Flight Price
        self.price = int(flight_data.get('price'))

        # Stop Overs
        self.stop_overs = stop_overs

        # Via City
        self.via_city = flight_data['route'][0].get('cityTo', None)
