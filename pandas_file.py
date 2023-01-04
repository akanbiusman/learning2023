import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels)
print(red_squirrels)
print(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_counts.csv")

# data = pandas.read_csv("file.csv")
#
# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
#
# # get data in columns
# print(data.condition)
# print(data["condition"])

# get data in rows
# print(data[data.day == "monday"])

# get data from row where temp is at maximum
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)
#
