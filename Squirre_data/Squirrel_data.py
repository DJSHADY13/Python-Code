import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = data.to_dict()

fur_color = data["Primary Fur Color"].to_list()

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

color_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray, cinnamon, black]
}

dat = pandas.DataFrame(color_dict)

dat.to_csv("Fur Color")