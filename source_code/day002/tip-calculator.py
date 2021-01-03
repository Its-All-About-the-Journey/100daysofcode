print("Welcome to the tip calculator.")

# Get the bill total, check for valid input.
while True:
    try:
        total = float(input("What was the bill total? $"))
        break
    except ValueError:
        print("Please enter the bill total in decimal format (ie: 100.00)")

# Get the number of people, check for valid integer input.
while True:
    try:
        people = int(input("How many people are splitting the bill? "))
        break
    except ValueError:
        print("Please enter a whole number.")

# Get the tip percentage, check for valid input (10, 12, or 15).
while True:
    try:        
        tip_percent  = int(input("What percentage tip would you like to give: 10, 12, or 15? "))
        if tip_percent == 10 or tip_percent == 12 or tip_percent == 15:
            break
        else:
            print('You must enter 10, 12, or 15.')
    except:
        print('You must enter 10, 12, or 15.')
    
tip = total * (tip_percent/100)
total += tip

# Print payment per-person in 2-decimal format.
print(f"Each person should pay: ${format(round(total) / people, '.2f')}")