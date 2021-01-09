"""
Day 008 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/8/2021
"""

# Simple functions
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today!")


greet()

# Introduction to functions with parameters/arguments
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print("Isn't the weather nice today!")


greet_with_name("Wayne")

# Introduction to functions with multiple parameters and positional arguments
def greet_with(name, location):
    print(f"Welcome {name} to {location}!")


greet_with("Wayne", "Chicago")

# Using functions with keyword arguments
greet_with(location="Dubai", name="Wayne Kwiat")


# Ex 8.1 - Paint Area Calculator
import math


def paint_calc(height, width, cover):
    total_cans = (height * width) / cover
    print(f"You'll need {math.ceil(total_cans)} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

# Ex 8.2 - Prime number checker
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)