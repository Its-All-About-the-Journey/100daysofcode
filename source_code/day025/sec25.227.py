import pandas

FILENAME_IN = "./data/2018_squirrel_census.csv"
FILENAME_OUT = "./data/fur_counts.csv"

data = pandas.read_csv(FILENAME_IN)

#Fur Color, Count
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

# Save to csv
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data = pandas.DataFrame(data_dict)

data.to_csv(FILENAME_OUT)