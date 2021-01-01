# Get the total bill
bill = float(input("What's the total bill?: "))

#How much would you like to tip?
tip = float(input("What percentage tip would you like to give? 10, 12, or 15: "))

#How many ways should the bill be split?
split = int(input("How many ways do you want to split the bill?: "))

total_bill = (bill * (1 + (tip / 100)))

per_person = total_bill / split

per_person_rounded = round(per_person, 2)

#Print the final result
print(f"Each person should pay: ${per_person_rounded}")