from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from users import User

MAX_NUM_LAYOVERS = 3

# This file uses the DataManager,FlightSearch, FlightData, and
# NotificationManager classes to achieve the program requirements.

# Create DM class to get existing flight destination and price data from the google sheet
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()

# Create list of all IATA Code values
iata_codes = [destination['iataCode'] for destination in sheet_data]

# Create an instance of FS class (used later)
flight_search = FlightSearch()

# Check and see any IATA code value from the sheet is empty -> if one is, pass city name to FlightSearch Class
# to get correct IATA code -> Update sheet data and pass it back to data manager to update spreadsheet using sheety
if not all(iata_codes):
	print("Updating 1 or more IATA Codes...")
	for destination in sheet_data:
		# Update sheet_data dictionary using return_iata() method
		destination['iataCode'] = flight_search.return_iata(destination['city'])
	data_manager.update_iata()
	# Get the updated sheet_data and update the iata_codes
	sheet_data = data_manager.get_sheet_data()
	iata_codes = [destination['iataCode'] for destination in sheet_data]
else:
	print("IATA Codes are all up to date")

print("Iata Codes: ", iata_codes)
# Format iata codes in format required for flight search API (Comma separated IATA codes)
iata_codes_string = ','.join(iata_codes)
print("Iata Codes String: ", iata_codes_string)

# Make call to get_flights using destination iata codes string and save data to variable -> 0 layover flights only
flights = flight_search.get_flights(iata_codes_string, max_layovers=0)

# Create a list of all destination city names we wanted flights for
destination_cities = [destination['city'] for destination in sheet_data]
# Create a list of all destination city names we actually found flights for
flights_found_for = [destination['cityTo'] for destination in flights]
# Compare the two and determine which cities we did not find flights for ->
# generate a list to be used in a flight search with expanded layover parameters
flights_not_found = list(set(destination_cities).difference(set(flights_found_for)))
# Convert list of flights not found back to IATA codes
not_found_iatas = [destination['iataCode'] for destination in sheet_data if destination['city'] in flights_not_found]
# Convert to string format required by method and API
not_found_iatas = ','.join(not_found_iatas)
# Pass those IATA codes back into the flight search method, increasing number of allowed layovers
flights_with_layovers = flight_search.get_flights(not_found_iatas, max_layovers=MAX_NUM_LAYOVERS)

# Pass flights without layovers to flight_data class for processing
flight_data_manager = FlightData(flights, max_layovers=0)
# Print flight prices
flight_data_manager.print_flight_prices()

# Pass flights with layovers to flight_data class for processing
flight_data_manager2 = FlightData(flights_with_layovers, max_layovers=MAX_NUM_LAYOVERS)
# Print flight prices
flight_data_manager2.print_flight_prices()

# Get flight data in compact format (see sample_compact_flight_data.json for structure) for flights without layovers
compact_flight_data = flight_data_manager.get_formatted_flight_data()
print('\n', compact_flight_data, '\n')
# Get flight data in compact format for flights with layovers
compact_flight_data2 = flight_data_manager2.get_formatted_flight_data()
print('\n', compact_flight_data2, '\n')

# Get user data from Users spreadsheet
user_data = User().get_users()
print('\n', user_data, '\n')

# Initialize instance of notification manager passing in sheet data and flight data for flights without layovers
notification_manager = NotificationManager(sheet_data, compact_flight_data)
# Call function to compare sheet data to flight data and notify via SMS and email if lower price is found
notification_manager.compare_prices_and_notify(user_data, has_layovers=False)
# Initialize instance of notification manager passing in sheet data and flight data for flights with layovers
notification_manager2 = NotificationManager(sheet_data, compact_flight_data2)
# Call function to compare sheet data to flight data and notify via SMS and email if lower price is found
notification_manager2.compare_prices_and_notify(user_data, has_layovers=True)

print("Program finished executing. If cheap flights have been found, you will receive a text and users will be "
      "emailed. Otherwise, try again later or adjust your price points")
