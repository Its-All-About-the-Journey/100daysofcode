from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

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
else:
	print("IATA Codes are all up to date\n")

# Format iata codes in format required for flight search API (Comma separated IATA codes)
iata_codes_string = ','.join(iata_codes)
# Make call to get_flights using destination iata codes string and save data to variable
flights = flight_search.get_flights(iata_codes_string)
# Pass data to flight_data class for processing
flight_data_manager = FlightData(flights)
# Print flight prices
flight_data_manager.print_flight_prices()

# Get flight data in compact format (see sample_compact_flight_data.json for structure)
compact_flight_data = flight_data_manager.get_formatted_flight_data()

# Initialize instance of notification manager passing in sheet data and flight data
notification_manager = NotificationManager(sheet_data, compact_flight_data)
# Call function to compare sheet data to flight data and notify via SMS if lower price is found
notification_manager.compare_prices_and_notify()

