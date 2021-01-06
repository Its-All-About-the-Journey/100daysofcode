import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# shuffle the letters data set and pull out the required number of them
random.shuffle(letters)
pw_letters = letters[:nr_letters]

# do it again but for numbers
random.shuffle(numbers)
pw_numbers = numbers[:nr_numbers]

# and then again for symbols
random.shuffle(symbols)
pw_symbols = symbols[:nr_symbols]

# bring all three together in one list
password = pw_letters + pw_numbers + pw_symbols

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print(f"Easy Level Passowrd: {''.join(password)}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password)
print(f"Hard Level Passowrd: {''.join(password)}")