"""
Day 009 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/9/2021
"""

# Introduction to Dictionaries
# dictionary_name = {key:value,...}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program form running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from the dictionary.
print(programming_dictionary["Bug"])

# Adding new items - define new key name and assign value
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating an empty dictionary.
empty_dict = {}

# Editing an item in a Dictionary
# programming_dictionary["Bug"] = "A mouth in your computer!"

# Looping through a dictionary
for key in programming_dictionary:
    # Prints only the key
    print(key)
    # Prints the value
    print(programming_dictionary[key])

# Ex. 9.1 - Grading Program
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"
    elif 81 <= student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# Ex 9.2 Working with Nested data
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


def add_new_country(country_visited, num_visits, cities_to_add):
    new_country = {"country": country_visited, "visits": num_visits, "cities": cities_to_add}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
