#Password Generator Project - "Hard Level"
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = [random.choice(letters) for i in range(nr_letters)]
for i in range(nr_symbols): password.append(random.choice(symbols))
for i in range(nr_numbers): password.append(random.choice(numbers))

# Removed use of 2nd and 3rd list comps because unused return list = wasteful
# [password.append(random.user_selection(symbols)) for i in range(nr_symbols)]
# [password.append(random.user_selection(numbers)) for i in range(nr_numbers)]

random.shuffle(password)
password = ''.join(password)

print(f'Here is your password: {password}')
