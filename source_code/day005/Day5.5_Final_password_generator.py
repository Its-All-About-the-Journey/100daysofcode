#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passchar = []
password0 = ""
for x in range(0, nr_letters):
  passchar.append(letters[random.randint(0,53)])
# or use: passchar.append(random.choice(letters))
for x in range(0,nr_symbols):
  passchar.append(symbols[random.randint(0,8)])
# or use: passchar.append(random.choice(symbols))
for x in range(0,nr_numbers):
  passchar.append(numbers[random.randint(0,9)])
# or use: passchar.append(random.choice(numbers))
for x in range(0, len(passchar)):
  password0 += passchar[x]

print(f"\nYour simple password is: {password0}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password1 = ""

random.shuffle(passchar)

for char in passchar:
  password1 += char
print(f"\nYour randomized password is: {password1}")