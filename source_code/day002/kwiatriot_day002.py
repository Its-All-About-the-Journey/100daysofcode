"""
Day 002 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/2/2021
"""


# Data Types

# Strings
# Printing individual string characters
print("Hello"[4])

# Integer
# Use underscore (_) to substitute for commas to make human readable numbers
print(3_500 + 2_345)


# Ex 2.1 - Adding the digits of a number input by user
two_digit_number = input("Type a two digit number: ")
digits_added = int(two_digit_number[0]) + int(two_digit_number[1])
print(digits_added)

# Ex 2.2 - BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height)**2
print(int(bmi))

# Ex 2.3 - Days, Weeks, Months remaining if you lived to 90
age = input("What is your current age?")
age_int = int(age)
total_days = 365 * 90
total_weeks = 52 * 90
total_months = 12 * 90

days_left = total_days - (age_int * 365)
weeks_left = total_weeks - (age_int * 52)
months_left = total_months - (age_int * 12)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

# Day 2 Final Project - Tip Calculator
print("Welcome to the tip calculator!")
total_bill = input("What is the total bill? $")
tip_percent = input("What percentage tip would you like to leave? 10, 12, or 15? ")
total_people = input("How many people split the bill? ")

result = round((float(total_bill) / int(total_people)) * (int(tip_percent) / 100 + 1),2)
result_formatted = "{:.2f}".format(result)
print(f"Each person should pay: ${result_formatted}")
