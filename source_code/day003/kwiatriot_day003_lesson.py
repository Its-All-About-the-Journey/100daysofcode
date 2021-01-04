"""
Day 003 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/3/2021
"""

# Ex 3.1, if/else conditional - checking to see if a number is odd or even
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")

# Ex 3.2, elif conditional - BMI revisited
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height**2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# Ex 3.3, if/else practice - Determining a leap year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 > 0:
        print("Leap year.")
    elif year % 400 == 0:
        print("Leap Year.")
    else:
        print("Not Leap Year.")
else:
    print("Not Leap Year.")


# EX 3.4 - Pizza Cost Calculator
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    if add_pepperoni == "Y":
        bill += 17
    else:
        bill += 15
elif size == "M":
    if add_pepperoni == "Y":
        bill += 23
    else:
        bill += 20
else:
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Ex. 3.5 - Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names = name1.lower() + name2.lower()

true_count = 0
love_count = 0

true_count += combined_names.count("t")
true_count += combined_names.count("r")
true_count += combined_names.count("u")
true_count += combined_names.count("e")

love_count += combined_names.count("l")
love_count += combined_names.count("o")
love_count += combined_names.count("v")
love_count += combined_names.count("e")

love_score = int(str(true_count) + str(love_count))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
