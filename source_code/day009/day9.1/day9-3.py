travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Frankfurt"], "total_visits": 4}
} 

print(travel_log)

#Nesting a dictionary in a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Frankfurt"],
        "total_visits": 4
    },
]