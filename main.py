import pandas

# data = pandas.read_csv("file.csv")
#
# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

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
