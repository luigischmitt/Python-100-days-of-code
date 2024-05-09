# with open ("Python-100-days-of-code/day 25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open ("Python-100-days-of-code/day 25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

import pandas as pd

df = pd.read_csv("Python-100-days-of-code/day 25/weather_data.csv")

# print(df.info())
# print(df)

# temp_list = df["Temperature"].to_list()
# print(len(temp_list))

# mean = sum(temp_list) / 7
# print(f"Mean temperatura this week: {mean:.2f}")

# Get data in columns
# print(df["Condition"])

# Get data in rows
# monday = df[df["Day"] == "Monday"]
# monday_temp = monday.Temperature[1]
# monday_temp_F = monday_temp * 9/5 + 32
# print(f"Monday temperature is {monday_temp_F}F")

# Create a Dataframe from scratch
data_dict = {
    "students": ["Luigi", "José", "Bia", "Geo"],
    "scores": [72, 83, 56, 56]
}

df = pd.DataFrame(data_dict)
print(df)

df.to_csv("new_data.csv")
