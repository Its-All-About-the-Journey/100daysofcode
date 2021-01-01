#1. Create a greeting for your program.
print("Anthony's Band Name Generator!")
print("=" * 80)
print()

#2. Ask the user for the city that they grew up in.
city_name = input("What city are you from?\n")
print()

#3. Ask the user for the name of a pet.
pet_name = input("What pet name do you like most?\n")
print()

#4. Combine the name of their city and pet and show them their band name.
band_name = f"{city_name} {pet_name}"
print(f"Your band name should be {band_name}")

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/