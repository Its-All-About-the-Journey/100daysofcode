# 🚨 The Python Dictionary: Deep Dive 👇

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

# Retrieving items from a dictionary.
print(programming_dictionary["Bug"])

# Adding new items into a dictionary.
programming_dictionary["Python"] = "Python is an interpreted, high-level and general-purpose programming language."
print(programming_dictionary)

# Create an Empty Dictionary
empty_dictionary = {}

# Add items to an Empty Dictionary
empty_dictionary[""] = ""

# Wipe and existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary, this method only provides the key
for thing in programming_dictionary:
    print(thing)

# Loop through a dictionary and print out Key and Value
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])