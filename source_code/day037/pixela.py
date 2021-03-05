import requests
from datetime import datetime
import os

PIXELA_TOKEN = os.environ['PIXELA_TOKEN']
USER = os.environ['PIXELA_USER']

graph_id = 'graph1'

post_headers = {
    'X-USER-TOKEN' : PIXELA_TOKEN
}

#Create a user

''''
pixela_user_params = {
    "token" : PIXELA_TOKEN,
    "username" : USER,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

pixela_users_url = "https://pixe.la/v1/users"

response = requests.post(url=pixela_users_url, json=pixela_user_params)

print(response.text)
'''
# Create a graph

'''
graph_params = {
    "id":"graph1",
    "name":"Days Of Code",
    "unit":"commits",
    "type":"int",
    "color":"shibafu"
    }

pixela_graph_url = "https://pixe.la/v1/users/trynius/graphs"

response = requests.post(url=pixela_graph_url, headers=post_headers, json=graph_params)
print(response.text)

'''

#Post a Value
'''
pixela_post_data_url = f"https://pixe.la/v1/users/{USER}/graphs/{graph_id}"

#today = datetime(year=2021,month=3,day=1)
today = datetime.today().strftime('%Y%m%d')

pixela_post_data_params = {
    "date":today,
    "quantity":"1",
}

response = requests.post(url=pixela_post_data_url, headers=post_headers, json=pixela_post_data_params)

'''
#Update a Value
'''
#today = datetime(year=2021,month=3,day=1)
today = datetime.today().strftime('%Y%m%d')

pixela_post_data_url = f"https://pixe.la/v1/users/{USER}/graphs/{graph_id}/{today}"


pixela_post_data_params = {
    "quantity":"4",
}

requests.put(url=pixela_post_data_url, headers=post_headers, json=pixela_post_data_params)

'''
#Increment/Decrement Today's Value

'''
#pixela_post_data_url = f"https://pixe.la/v1/users/{USER}/graphs/{graph_id}/increment"
pixela_post_data_url = f"https://pixe.la/v1/users/{USER}/graphs/{graph_id}/decrement"

requests.put(url=pixela_post_data_url, headers=post_headers)
'''

#Delete a Value
'''
#today = datetime(year=2021,month=3,day=1)
today = datetime.today().strftime('%Y%m%d')

pixela_post_data_url = f"https://pixe.la/v1/users/{USER}/graphs/{graph_id}/{today}"

requests.delete(url=pixela_post_data_url, headers=post_headers)

'''