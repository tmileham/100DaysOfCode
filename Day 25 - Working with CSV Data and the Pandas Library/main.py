# with open(
#     "Day 25 - Working with CSV Data and the Pandas Library/weather_data.csv"
# ) as weatherdata:
#     data = weatherdata.readlines()

# print(data)

# Working with CSV - using built in CSV module
# import csv

# temperatures = []

# with open(
#     "Day 25 - Working with CSV Data and the Pandas Library/weather_data.csv"
# ) as data_file:
#     temperatures = []
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas as pd

data = pd.read_csv(
    "Day 25 - Working with CSV Data and the Pandas Library/weather_data.csv"
)

# # Convert Pandas DataFrame to Python Dict
# data_dict = data.to_dict()

# print(data_dict)
# print("\n")

# # Convert Pandas Series to Python List
# data_list = data["temp"].to_list()

# print(data_list)

# # Calc mean average using Python Functions
# average_temp = sum(data_list) / len(data_list)
# print(round(average_temp))


# # Calc max value in a Series
# print(data["temp"].max())


# # Get Data in Columns
# print(data["condition"])
# print(data.condition)


# Get Data in Rows
print(data[data.day == "Monday"])
print("\n--------------")
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print("\n--------------")
print(monday.condition)

celcius = int(monday.temp)

fahrenheit = celcius * 1.8 + 32

print(f"Celcius: {celcius}")
print(f"Fahrenheit: {fahrenheit}")


# Create a dataframe from scratch

data_dict = {"students": ["Tom", "Keeley", "Kane", "Lee"], "scores": [99, 44, 33, 22]}

data = pd.DataFrame(data_dict)
data.to_csv("Day 25 - Working with CSV Data and the Pandas Library/new_data.csv")
print(data)