
print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n>>$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15%?\n>>"))
split = int(input("How many people would you like to split the bill?\n>>"))

bill_w_tips = round(tip / 100 * bill + bill, 2)
total_split = bill_w_tips / split


print(f"Each person have to pay: ${total_split}")
