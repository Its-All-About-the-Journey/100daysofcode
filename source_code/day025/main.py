#with open("source_code/day025/weather_data.csv", "r") as data:
#    weather = data.readlines()
#print(weather)
'''
import csv


with open("source_code/day025/weather_data.csv", "r") as data:
    next(data)
    weather = csv.reader(data)
    temperatures = []
    for row in weather:
        temperatures.append(int(row[1]))
    print(temperatures)
'''

import pandas
df = pandas.read_csv("source_code/day025/weather_data.csv")
#print((df["temp"]).to_string(index=False))

#data_dict = df.to_dict()
#print(data_dict)

#temp_list = df["temp"].to_list()
#print(temp_list)

#average_temp = sum(temp_list)/len(temp_list)
#average = round(df["temp"].mean())
#print(average)
#print(round(average_temp))

#max_temp = df["temp"].max()
#print(max_temp)

# Get data from columns
#print(df.condition)

# Filter data for specific row
#print(df[df.day == "Monday"])
#print(df.temp[df.temp == df.temp.max()])

# Get Monday's temperature in Fahreinheit
#temp = int(df.temp[df.day == "Monday"])
#fahrenheit = (temp * (9/5)) + 32
#print(fahrenheit)

#Create Dataframe from Scratch
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores" : [76, 56, 65]
#}

#new_df = pandas.DataFrame(data_dict)
#print(new_df)
#new_df.to_csv("source_code/day025/new_data.csv")

#CSV squirrel_count
#Small Table (Primary Fur Color) column, how many gray, how many cinnamon, how many black, build a new DF

#Columns:
#Fur Color, Count
squirrel_df = pandas.read_csv("source_code/day025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count = squirrel_df["Primary Fur Color"].value_counts()
df = pandas.DataFrame({'Fur Color':count.index, 'Count':count.values})
df.to_csv("source_code/day025/squirrel_count.csv")


# Official Method
grey_squirrels = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrel_df[squirrel_df["Primary Fur Color"] == "Black"])

df = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels, cinnamon_squirrels, black_squirrels]
}

newer_df = pandas.DataFrame(df)
print(newer_df)