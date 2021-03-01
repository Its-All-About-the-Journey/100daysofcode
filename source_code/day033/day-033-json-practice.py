import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

print(response)
print(response.content)
data = (response.json())

print(data)

print(data["iss_position"])
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (longitude,latitude)
print(iss_position)