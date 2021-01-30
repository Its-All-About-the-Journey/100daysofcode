# 🚨 Nesting Lists and Dictionaries 👇

# Dictionary Example #1
# {Key:Value}

# Dictionary Example #2
# {
#   Key:Value,
#   Key2:Value2,
# }

# Dictionary w/ Nested List or Dictionary
#{
#   Key: [List],
#   Key2:{Dict},
# }

# Sample Dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#You can nest a list within a list but it is not as useful
["A", "B", ["C", "D"]]

#Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "United States": {"states_visited": ["New York", "New Jersey", "Connecticut", "Pennsylvania", "Delaware", "Maryland", "Virginia", "West Virginia", "Florida", "Nebraska", "Iowa", "Tennessee", "Oklahoma", "Texas", "Arizona", "Colorado", "Arkansas", "Rhode Island"], "remaining_states": 32},
}

#Nesting a Dictionary in a List
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    },
]