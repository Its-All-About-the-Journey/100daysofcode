# DAY 8

Caesar Cipher

# Description

# Environment
OS: Ubuntu Bionic

Python version: 3.6.9

# Dependencies

None

# How to run script
```
Launch the program, and follow the prompts to receive your encoded message, or decode a message which has already been encoded.
```

# Sample output
```

 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"'"'"'"  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP"'""'"" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
asdfwxyz
Type the shift number:
5
The encoded text is fxikbcde
Give 'er another go? Type 'yes' to try again. :yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
fxikbcde
Type the shift number:
5
The decoded text is asdfwxyz
Give 'er another go? Type 'yes' to try again. :n
```

# Other Exercises

## Functions with Inputs
```
def greet():
  print("a")
  print("b")
  print("c")

def greet_by_name(name):
  print(f"""Aasdf, {name}""")
  print("Qrrbrbilbiel")
  print(f"""{name} - qwertsys""")

greet()
greet_by_name(input("Name: "))

```
## Arguements
```
def greet_with(name, location):
  print(f"""Flour, {name}""")
  print(f"""Water, brown sugar, and {location}?""")
  print(f"""Salt.""")

# Traditional implicit arguements
greet_with(input("Name: "), input("Location: "))

# Keyword Arguements
name_in = input("Name: ")
location_in = input("Location: ")
greet_with(location = location_in, name = name_in)
```

## Paint Can Calculator

The video suggests the ceiling function from the math library, math.ceil()

```
def paint_calc(height, width, cover):
  area_to_cover = height * width
  if area_to_cover % cover:
    cans = (area_to_cover // cover + 1)
  else: 
    cans = (area_to_cover // cover)
   
  print(cans)
```

## Prime Number Checker
```
# Prime Number Checker
# I'll be honest I did not remember how to do this so I looked it up.
# The wikipedia article on prime number was not helpful here either.
# Later I realized it is more simple than I thought it was.
def prime_checker(number):
  is_prime = True
  for iter in range (2,number):
    if number % iter == 0:
       print(f"""{number} is NOT a prime number, it is divisible by {iter}.""")
       is_prime = False
       break
  if is_prime:
    print(f"""{number} is a prime number.""")
  
```


