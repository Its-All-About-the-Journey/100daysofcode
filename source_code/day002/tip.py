print("Welcome to the tip calculator.")

bill = int(input("What was the total bill? $"))
#while bill != type(int) or type(int):
 #   bill = input("Please enter a number")

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? %"))
#while tip != 10 or 12 or 15:
 #   tip = input("Please enter a tip percentage of 10, 12 or 15. %")

split = int(input("How many people to split the bill? "))
#while split != type(int) or type(int):
 #   split = input("Please enter a number")

newTip = tip / 100
newTotal = bill + (bill * newTip)
indvBill = newTotal / split
roundedBill = round(indvBill, 2)

print(f"Each person should pay: ${roundedBill}")

