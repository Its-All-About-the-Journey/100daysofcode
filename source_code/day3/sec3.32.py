print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
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
        bill = 5
        print("Children tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age > 18:
        bill = 12
        print("Adult tickets are $12.")
    
    photos = input("Would you like photos for an additional $3? Yes or No: ")

    if photos == "Y" or "YES" or "Yes" or "y" or "yes":
        bill += 3

    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, you are not tall enough to ride the roller coaster!")
