#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = list()

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for _ in range(nr_letters):
    password.append( random.choice(letters) )

for _ in range(nr_symbols):
    password.append( random.choice(symbols) )

for _ in range(nr_numbers):
    password.append( random.choice(numbers) )

print('='*80)
print (f'Weak Password - {len(password)} chars')
print( ''.join(password) )
print()

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

scrambled_password = list()

for _ in range( len(password) ):
    rand_index = random.randint(0, len(password) - 1 )
    rand_char = password.pop(rand_index)
    scrambled_password.append(rand_char)


print(f'Strong password - {len(scrambled_password)} chars')
print( ''.join(scrambled_password) )
print('='*80)