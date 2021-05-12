from datetime import datetime, timedelta

# This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self, raw_flight_data, max_layovers=0):
        self.flight_data = raw_flight_data
        self.departure_city = self.flight_data[0]['cityFrom']
        self.departure_airport_codes = [destination['flyFrom'] for destination in self.flight_data]
        self.destination_cities = [destination['cityTo'] for destination in self.flight_data]
        self.destination_airport_codes = [destination['flyTo'] for destination in self.flight_data]
        self.prices = [destination['price'] for destination in self.flight_data]
        self.nights_in_destinations = [destination['nightsInDest'] for destination in self.flight_data]
        self.max_layovers = max_layovers

        # Get departure date from flight_data and format in Murica' format (MM/DD/YYYY without leading zeroes)
        self.departure_dates = []
        for destination in self.flight_data:
            departure_date_string = destination['route'][0]["local_departure"].split('T')[0]
            formatted_date = datetime.strptime(departure_date_string, '%Y-%m-%d').strftime('%#m/%#d/%Y')
            self.departure_dates.append(formatted_date)

        # Get return date from flight_data and format in Murica' format (MM/DD/YYYY without leading zeroes)
        self.return_dates = []
        for destination in self.flight_data:
            return_date_string = destination['route'][1]["local_departure"].split('T')[0]
            formatted_date = datetime.strptime(return_date_string, '%Y-%m-%d').strftime('%#m/%#d/%Y')
            self.return_dates.append(formatted_date)

        # For flights with layovers, create a number of other instance attributes...
        if self.max_layovers > 0:

            # Create a nested list of layover cities for one-way flight to each of the destinations
            self.outbound_layover_cities = []
            for destination in self.flight_data:
                layover_cities = []
                for leg in destination['route']:
                    if leg['return'] == 0 and leg['cityTo'] != destination['cityTo']:
                        layover_cities.append(leg['cityTo'])
                self.outbound_layover_cities.append(layover_cities)

            # Create a nested list of layover cities for return flight from each destination
            self.return_layover_cities = []
            for destination in self.flight_data:
                layover_cities = []
                for leg in destination['route']:
                    if leg['return'] == 1 and leg['cityTo'] != destination['cityFrom']:
                        layover_cities.append(leg['cityTo'])
                self.return_layover_cities.append(layover_cities)

        # Consolidate info for all flights into compact list
        self.formatted_flight_data = []
        for i in range(len(self.destination_cities)):
            self.formatted_flight_data.append({'departure_city': self.departure_city,
                                               'departure_airport_code': self.departure_airport_codes[i],
                                               'arrival_city': self.destination_cities[i],
                                               'arrival_airport_code': self.destination_airport_codes[i],
                                               'price': self.prices[i],
                                               'departure_date': self.departure_dates[i],
                                               'return_date': self.return_dates[i],
                                               'nights_in_destination': self.nights_in_destinations[i]})
            if self.max_layovers > 0:
                self.formatted_flight_data[i].update(
                    {'num_outbound_layovers': len(self.outbound_layover_cities[i]),
                     'outbound_layover_cities': self.outbound_layover_cities[i],
                     'num_return_layovers': len(self.return_layover_cities[i]),
                     'return_layover_cities': self.return_layover_cities[i]})

    # Function prints out the cheapest ticket to fly to destinations declared in google sheet -> Also, prints
    # additional layover information for flights that have layovers
    def print_flight_prices(self):
        print(f"\nThe cost to fly from {self.departure_city} to your destinations are as follows:\n")
        for i in range(len(self.destination_cities)):
            print(f"{self.destination_cities[i]} ({self.destination_airport_codes[i]}) via "
                  f"{self.departure_airport_codes[i]} airport: ${self.prices[i]}")
            if self.max_layovers > 0:
                print(f'Outbound flight has {len(self.outbound_layover_cities[i])} layover(s) via '
                      f'{" and ".join(self.outbound_layover_cities[i])}')
                print(f'Return flight has {len(self.return_layover_cities[i])} layover(s) via '
                      f'{" and ".join(self.return_layover_cities[i])}\n')

    # Function returns the compact/formatted flight data for all destinations
    def get_formatted_flight_data(self):
        return self.formatted_flight_data
