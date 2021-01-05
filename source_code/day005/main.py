#!/usr/bin/env python3
# 100 Days of Code : Day 5 Project
# Password Generator
# Adam Pawlowski (@hypermanganate)

# Main
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = '' 
vars = {'nr_letters': letters, 'nr_symbols': symbols, 'nr_numbers': numbers}

for var in vars:
  for iter in range(0, globals()[var]):
    password += vars[var][random.randint(0, len(vars[var]) - 1)]

print(f"""\n\nYour password is: {password}""")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# I"m guessing what they meant here is to say, decide if you want 0/1/2 letter/number/symbol and dip from that pool as you select the random characters.
# I chose instead to randomize the contents of the existing password, which feels like the list should have a 'shuffle' method but it does not.
# EDIT: I have since watched the video and there is a shuffle, but it is in random. Well, dang. They also used .choice() which also would have been easier.

order = range(0, len(password))
list_password = []
new_password = ''

for number in order:
  list_password.append(password[number])

for iter in order:
  index = random.randint(0, len(list_password) - 1)
  new_password += list_password[index]
  list_password.remove(list_password[index])

print(f"""\nYour _boss level_ password is: {new_password}""")

print("\n*** Password Analysis ***\n")

bad_diss = ["my grandma can crack that code", "my luggage has a stronger password", "I wouldn't secure my gym locker with that one"]
good_password = ["Not only is it hard to guess, but it's hard to remember!", "It'll take the FSB a while to crack that one!", "You're not messing around!"]

if len(password) < 8:
  print(f"""You can't be serious, {bad_diss[random.randint(0,2)]}.""")
elif len(password) == 8:
  print(f"""Great password for a mainframe, 20 years ago.""")
elif len(password) < 16:
  print(f"""Not bad! {good_password[random.randint(0,2)]}.""")
else:
  print(f"""That one's so secure I hope you'll write it down twice - just to be safe.""")
