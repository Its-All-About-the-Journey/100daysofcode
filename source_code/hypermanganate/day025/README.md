
# DAY 25

50 States Guessing Game

# Description

See if you cna guess all 50 states in the US (excluding, districts, territories, autonomous zones, etc)

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7 

# Dependencies

Pandas 1.2.1

# How to run script
```
Call the script

Enter some states and see if you can guess them all

When you've given up, type "exit"

A CSV file of states you need to review will be provided as "states_to_learn.csv"
```

# Sample output

![Sample of Game](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day025/50_states_game.png)

# Other Exercises
## Read using CSV and extract a value:

```
import csv

temperatures = []

weather_data = csv.reader(open("./weather_data.csv", mode="r"))
for data in weather_data:
    temperatures.append(data[1])
temperatures.remove("temp")

print(temperatures)
```

## How many Squirrels by color
```
import pandas

# Grab DataFrame from CSV
squirrels = pandas.read_csv("./squirrel_data.csv")

# Create a new data frame from the Series
data_extract = squirrels["Primary Fur Color"].value_counts().reset_index()

# Set new column names
data_extract.columns = ['Primary Fur Color', 'Count']

# Print CSV representation
print(data_extract.to_csv())

```