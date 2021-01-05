# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Congratulations, you've got a job at Python Pizza. 
# Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M, or L
# Do you want pepperoni? Y or N
# Do you want extra cheese? Y or N

#Write your code below this line 👇

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your pizza comes out to ${bill}.")

# sm_bill = 0
# med_bill = 0
# lg_bill = 0

# if size == "S":
#     sm_bill = 15
#     if add_pepperoni == "Y" and size == "S":
#         sm_bill += 2
#         if extra_cheese == "Y":
#             sm_bill +=1
#             print(f"Your total comes out to ${sm_bill}.")
# elif size == "M":
#     med_bill = 20
#     if add_pepperoni == "Y" and size != "S":
#         med_bill += 3
#         if extra_cheese == "Y":
#                 med_bill +=1
#                 print(f"Your total comes out to ${med_bill}.")
# elif size == "L":
#     lg_bill = 25
#     if add_pepperoni == "Y" and size != "S":
#         lg_bill += 3
#         if extra_cheese == "Y":
#             lg_bill +=1
#             print(f"Your total comes out to ${lg_bill}.")

# else:
#     print("Thank you for stopping by.")