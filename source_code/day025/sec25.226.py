import pandas

FILENAME = "weather_data.csv"

if __name__ == "__main__":
    # Reads csv file
    data = pandas.read_csv(FILENAME)

    # Converting the data into a python dict
    data_dict = data.to_dict()

    # Printing dict
    print("=" * 79)
    print(f"Data to dict:\n\n{data_dict}")

    # Converting the temp column called a series into a python list
    data_temp_series = data["temp"].to_list()

    print("=" * 79)
    print(f"Temperature data:\n\n{data_temp_series}")

    # Manually calculating the average
    avg = sum(data_temp_series) / len(data_temp_series)

    print("=" * 79)
    print(f"Average temperature calculating: {avg}")

    # Using panda to calculate the average with the mean method
    print("=" * 79)
    print(f"Average temperature using Pandas series mean: {data['temp'].mean()}")

    # Using panda to search for the max temp value
    print("=" * 79)
    print(f"Max temperature using Pandas series max: {data['temp'].max()}")

    # Using a panda condition to get the row with the max temp
    print("=" * 79)
    print("Day with max temperature")
    print(data[data.temp == data.temp.max()])

    # Using panda to extract the row that contains Monday
    monday = data[data.day == "Monday"]

    # Using panda, get the mondays temp and convert to celsius
    print("=" * 79)
    print(f"Mondays temperature: {int(monday.temp) * 9/5 + 32} celsius")
  
    # Creating a dataframe
    data_dict = {
        "students": ["Amy", "James", "Angela"], 
        "scores": [75, 76, 65]
    }

    # Creating a panda dataframe from a python dict
    data = pandas.DataFrame(data_dict)
    print("=" * 79)
    print(data)

    print("=" * 79)

    # Output data to a csv file
    data.to_csv("new_data.csv")