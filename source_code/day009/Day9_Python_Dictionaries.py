programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}
#Retrieve a value from a dictionary by referencing the key:
#Make sure your data types match!!!!
print(programming_dictionary["Bug"])
#Add to the dictionary:
programming_dictionary["Loop"] = "The action of doing something over and over again"
#Create new dictionary:
new_dictionary = {}
#Erase an existing:
#programming_dictionary = {}

#Edit a value for an existing key in an existing dictionary:
programming_dictionary["Bug"] = "A moth in your computer"

#Looping through a dictionary loops through the keys:
for each in programming_dictionary:
  print(each)
  #now that we have the key we can print the value:
  print(programming_dictionary[each])

#Nesting within dictionaries:
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}
#Nesting a list in a dictionary:
travel_log = {
  "France": ["Paris", "Lille", "Dijon"]
}
#Nesting a dictionary in a dictionary:
travel_log = {
  "France": {"Cities_Visited": ["Paris", "Lille", "Dijon"],
             "total_visits": 12}
}
print(travel_log["France"]["total_visits"])

#Nest multiple dictionaries inside a list:
travel_log = [
  {
    'country': 'France',
    'cities_visited': ['Paris', 'Lille', 'Dijon'],
    'total_visits': 12
  },
  {
    'country': 'Germany',
    'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
    'total_visits': 5
  }
]

print("I visited the following cities in each of these countries:")

for each_dict in travel_log:
  city_list = ""
  for cities in each_dict["cities_visited"]:
    city_list += cities + ', '
  print(f"In {each_dict['country']}: {city_list}{each_dict['total_visits']} times.")
