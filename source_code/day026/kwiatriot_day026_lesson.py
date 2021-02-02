"""
Day 026 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 2/1/2021
"""

# Introduction to list comprehensions
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # list comp syntax is new_list = [new_item for item in list if test]
# squared_numbers = [n ** 2 for n in numbers]
#
# print(squared_numbers)
#
# numbers_2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [even_num for even_num in numbers_2 if even_num % 2 == 0]
# print(result)

# with open("file1.txt") as file1:
#     file_1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     file_2 = file2.readlines()
#
# result = [int(num) for num in file_1 if num in file_2]
#
# print(result)

# # Intro to Dict comprehension
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {string: len(string) for string in sentence.split()}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)


