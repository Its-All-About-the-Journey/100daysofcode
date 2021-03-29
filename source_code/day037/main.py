import requests
from datetime import datetime
import os

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
PIXELA_USERNAME = 'grantarmy89'
PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
PIXELA_GRAPH_ID = 'graph1'

# Parameters to make end user account on pixela
pixela_parameters = {
	"token": PIXELA_TOKEN,
	"username": PIXELA_USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes"
}

# Post request to create end user account on pixela
response = requests.post(url=PIXELA_ENDPOINT, json=pixela_parameters)
print(response.text)

GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs'
# Parameters to create graph
graph_parameters = {
	'id': PIXELA_GRAPH_ID,
	'name': 'Coding Graph',
	'unit': 'commit',
	'type': 'int',
	'color': 'sora'
}

headers = {
	'X-USER-TOKEN': PIXELA_TOKEN
}

# Post request to create graph
response = requests.post(url=GRAPH_ENDPOINT, json=graph_parameters, headers=headers)
print(response.text)

ADD_PIXEL_ENDPOINT = f'{GRAPH_ENDPOINT}/{PIXELA_GRAPH_ID}'

today = datetime.today().strftime('%Y%m%d')
yesterday = datetime(year=2021, month=3, day=29).strftime('%Y%m%d')

# Parameters to add pixel to graph
add_pixel_parameters = {
	'date': today,
	'quantity': '12'
}

# Post request to add pixel
response = requests.post(url=ADD_PIXEL_ENDPOINT, json=add_pixel_parameters, headers=headers)
print(response.text)

# Declaring a date to be used in our put request, which we will update the data for
change_date = datetime(year=2021, month=3, day=25).strftime('%Y%m%d')
UPDATE_PIXEL_ENDPOINT = f'{ADD_PIXEL_ENDPOINT}/{change_date}'

update_pixel_parameters = {
	'quantity': '14'
}

# Put request to update pixel for 3/25/2021
response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_parameters, headers=headers)
print(response.text)

# Using a delete request to delete a pixel on a certain day
delete_date = datetime(year=2021, month=3, day=26).strftime('%Y%m%d')
DELETE_PIXEL_ENDPOINT = f'{ADD_PIXEL_ENDPOINT}/{delete_date}'
response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
print(response.text)
