import csv

import pandas

if __name__ == "__main__":

    with open("weather_data.csv") as file_in:
        data = csv.reader(file_in)

        temperatures = list()

        for row in data:
            if row[1] != "temp":
                temperatures.append([row[0], int(row[1]), row[2]])
        
        print(temperatures)
        print()

    data = pandas.read_csv("weather_data.csv")
    print(data)