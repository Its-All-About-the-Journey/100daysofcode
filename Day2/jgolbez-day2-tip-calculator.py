#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill = float(input("Please enter the total bill amount:\n"))
tip_pct = int(input("Please enter the percentage of tip:\n"))
people = int(input("Please enter the number of people\n"))
adjbill = bill * (1 + (tip_pct * 0.01))
bill_split = round(adjbill / people, 2)
currency_value = ("{:.2f}".format(bill_split))
result = f"Each person should pay ${currency_value}"
print(result)