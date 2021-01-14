# DAY 13

Debugging

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

## Problem 1 - Insufficient Iteration

```
# Describe Problem
# It's expected to print "You got it" when reaching 20 in the interation, and the code reads that way. However in Python, some nut decided that the ending value of range is not included in the set.
def my_function():
  for i in range(1, 21):
#   print(i) # This reveals the values of i, where we can see that we don't reach the desired value due to the range statement being used incorrectly.
    if i == 20:
      print("You got it")
my_function()
```

## Problem 2 - Forgot that it's an index

```
# Reproduce the Bug

# while True: forces this code to execute until it crashes.
# I would argue to reproduce the bug, you'd have been informed one existed and this may not be needed. 
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # Unlike range, the pool of numbers includes the ending value. Potentially here we were thinking dice and not list.
print(dice_imgs[dice_num])
```

## Problem 3 - Millenials

```
# Play Computer
# The year 1994 ends up in limbo.
# I don't know about you but I'd rather not be a millenial personally so I will extend this to the 1994 persons.
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")
```

## Problem 4 - IDE indicated errors ... or not

```
# Fix the Errors
# When I uncommented this I don't see anything, but I disabled the intelligence in repl.it since it was irritating.
# A bit lame to just paste everything into Google as well, you could consider looking at it first.
age = int(input("How old are you?")) # Variable type was incorrect here
if age > 18:
  print(f"You can drive at age {age}.") # Block wasn't indented, string wasn't an f string or formatted.
```

## Problem 5 - Print

I wasn't sure what do to here. The example is that you can "debug" by monitoring value state and such with print(), but, the comparison operator should also be flagged typically as a warning in a case like this.
I use print like this often or logging or something, so I get it.

```
#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # Comparison and not assignment
total_words = pages * word_per_page
print(total_words)
```

## Problem 6 - Step Through Debugging

```
#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) ## This isn't in the block so we only assign once. 
  print(b_list)

mutate([1,2,3,5,8,13])
```

## Challenge 1 - Debug Odd or Even

Original:

```
number = int(input("Which number do you want to check?"))

if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
```

Problem:

Assignment operator is used (=) instead of comparitor.

Fix:

```
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
```

## Challenge 2 - Leap Year Debugging

Original:

```
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

```  

Problem:

Input is a string, which is not cast to numeric for mathematics

Solution:

I did not go back to see if this math follows the formula. 
If it does not, then this still has bugs.

```
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
```

## Challenge 3 - Debugging Fizz Buzz

Original:

```
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])
```

Problem:

Print statement contains brackets for no apparent reason.
The comparitor on "FizzBuzz" contains a logic error which is not particularly visible as elif was not used.
Change the or to and, and modify the logic tree so that it does not execute multiple statements per evaluating each iterator.

Solution:

```
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
```
