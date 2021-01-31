"""
Day 025 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/27/2021
"""

import csv
import pandas

# with open("weather_data.csv") as csv_data:
#     data = csv.reader(csv_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Creates a pandas data frame from the csv file
# data = pandas.read_csv("weather_data.csv")
# # Create a list from one series in the data frame and calculate list
# temp_list = data["temp"].to_list()
# avg = sum(temp_list) / len(temp_list)
# print(avg)
# # Using Pandas to do the average
# print(data["temp"].mean())
# # Finding max value is a pandas series
# print(data["temp"].max())
# Getting data from row
# monday = data[data.day == "Monday"]
# temp = int(monday.temp)
# f = (temp*9/5)+32
# print(f)

full_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sq_count = len(full_data[full_data["Primary Fur Color"] == "Gray"])
red_sq_count = len(full_data[full_data["Primary Fur Color"] == "Cinnamon"])
black_sq_count = len(full_data[full_data["Primary Fur Color"] == "Black"])
print(grey_sq_count)
print(red_sq_count)
print(black_sq_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_sq_count, red_sq_count, black_sq_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
