# Final - Bill and Tip Calculator
# ================================================

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calc")
subtotal = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you liket to give? "))
people = int(input("How many people to split the bill? "))

total = round(subtotal * ((tip / 100) + 1), 2)
individual = round(total / people, 2)

print(f"A {tip}% tip on ${subtotal} split {people} ways, yields ${individual}")