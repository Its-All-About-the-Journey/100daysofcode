import csv
import pandas

# # Getting Data with Pandas
data = pandas.read_csv('weather_data.csv')

# Printing the entire Panda Data Frame
print(type(data))

# Printing a single column or Panda Series
print(type(data['temp']))

# Converting the Data Frame to a dictionary and printing
data_dict = data.to_dict()
print(data_dict)


# Converting a Panda Series into a list
temp_list = data['temp'].to_list()

# Using Series methods built into Panda
print(data['temp'].mean())
# print(sum(temp_list)/len(temp_list))
print(data['temp'].max())

# Get Data by Columns (Series)
print(data['day'], '\n')
print(data.day, '\n')

# Get data by a specific row value
print(data[data.day == 'Monday'], '\n')
print(data[data.temp == data.temp.max()], '\n')

# Get data by specific row value, then filter further
monday = data[data.day == 'Monday']
print(monday.condition)

# Converting temperature to standard integer, then to fahrenheit
print(int(monday.temp) * 1.8 + 32)

# Creating a Data Frame from scatch
data_dict = {
  'students': ['Grant', "Joe Rogan", 'Jackie'],
  'scores': [69, 69, 69]
}
data2 = pandas.DataFrame(data_dict)
print(data2)

# Convert DataFrame to CSV
data2.to_csv('new_data.csv')


