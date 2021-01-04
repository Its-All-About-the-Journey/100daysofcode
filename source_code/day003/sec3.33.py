# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Add pizza size fee
if size == 'S':
  fee = 15

elif size == 'M':
  fee = 20

elif size == 'L':
  fee = 25

else:
  raise Exception(f'Error on pizza size input, received {size}, was expecting S, M, or L')

# Add Pepperoni fee
if add_pepperoni == 'Y':
    if size == 'S':
        fee += 2

    else:
        fee += 3

elif not (add_pepperoni == 'N'):
  raise Exception(f'Error on pepperoni input, received {add_pepperoni}, was expecting Y or N')

# Add extra cheese fee
if extra_cheese == 'Y':
    fee += 1

elif not (extra_cheese == 'N'):
  raise Exception(f'Error on extra cheese input, received {extra_cheese}, was expecting Y or N')

print(f'Your final bill is: {fee}.')


# Test cases:
#-----------------------------------------------------------------------------------------
#     S N N - 15
#     S N Y - 16
#     S Y N - 17
#     S Y Y - 18

#     M N N - 20
#     M N Y - 21
#     M Y N - 23
#     M Y Y - 24

#     L N N - 25
#     L N Y - 26
#     L Y N - 28
#     L Y Y - 29

#     A X X - Exception: Error on pizza size input, received A, was expecting S, M, or L
#     S A X - Exception: Error on pepperoni input, received A, was expecting Y or N
#     S Y A - Exception: Error on extra cheese input, received A, was expecting Y or N
