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
```

# Sample output
```
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


