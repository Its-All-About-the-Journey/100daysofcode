print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want: S, M or L? ").upper()
pepperoni = input("Do you want pepperoni? Y or N").upper()
extra_cheese = input("Do you want extra cheese? Y or N").upper()
total = 0
if size == "S":
    total += 15
elif size == "M":
    total += 20
else:
    total += 25

if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3

if extra_cheese == "Y":
    total += 1

print(f"Your final bill is ${format(total,'.2f')}.")