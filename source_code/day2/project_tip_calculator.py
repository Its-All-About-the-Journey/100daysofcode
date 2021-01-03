#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


# Welcome to the tip calculator
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $ ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

bill_as_int = float(bill)
tip_as_int = float(tip) / 100
tip_result = bill_as_int * tip_as_int
bill_tip_result = bill_as_int + tip_result
split_as_int = int(split)
split_results = bill_tip_result / split_as_int
split_round = round(split_results, 2)

print(f"Each person should pay: ${split_round}")

