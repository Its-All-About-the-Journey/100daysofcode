print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# Comparison Operators
# >     = greater than
# <     = lesser than
# <=    = lesser than or equal to
# >=    = greater than or equal to
# ==    = equal to
# !=    = not equal to

# Cost < 12 = $5
# Cost 12 - 18 = $7
# Cost > 18 = $12
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Your entrance fee is $5.")
    elif age <= 18:
        print("Your entrance fee is $7.")
    else:
        print("Your entrance fee is $12.")
else:
    print("Sorry, you are not tall enough to ride the roller coaster!")
