"""
Day 013 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/13/2021
"""
# Use a Debugger

# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        # Error was a wrong indent on the append function
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# Ex 13.1 - Debugging odd and even code
# number = int(input("Which number do you want to check?"))
#
# if number % 2 = 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

number = int(input("Which number do you want to check?"))
# error was with the = which is assignment not comparison
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Ex 13.2 - Debugging leap year code
# year = input("Which year do you want to check?")
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
# Error was wrong variable type for year, needed to convert to integer for comparison
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

# Ex 13.3 - Debugging FizzBuzz
# for number in range(1, 101):
#     if number % 3 == 0 or number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])

for number in range(1, 101):
    # Error was the use of 'or' when we should have been using 'and'
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # Error was wrong syntax of if/else block
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        # Error here was printing each number as a list, removed []
        print(number)
