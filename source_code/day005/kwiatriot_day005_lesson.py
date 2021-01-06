"""
Day 005 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/5/2021
"""

# Ex. 5.1 - Introduction to for loops, getting the average of a list
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

height_sum = 0
num_students = 0
for student in student_heights:
    height_sum += student
for people in student_heights:
    num_students += 1

height_avg = round(height_sum / num_students)
print(height_avg)

# Ex. 5.2 - for loop practice, getting highest value in a list
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")

# Ex. 5.4 - The 'ol FizzBuzz challenge
'''
The challenge is to print each number from 1 to 100. Whee the number is divisible by 3 the program should print 'Fizz'
When the number is divisible by 5 the program should print 'Buzz'
If the number is divisible by 3 and 5 the the program should print out 'FizzBuzz'
'''
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
