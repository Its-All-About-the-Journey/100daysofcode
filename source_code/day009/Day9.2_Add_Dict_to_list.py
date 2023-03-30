travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(new_country, num_visits, new_cities):
    travel_log.append({"country": new_country,
                   "visits": num_visits,
                   "cities": new_cities})
#or Angela's way:
#  country_add = {}
#  country_add["country"] = new_country
#  country_add["visits"] = num_visits
#  country_add["cities"] = new_cities
#  travel_log.append(country_add)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
