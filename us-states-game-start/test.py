import pandas


data = pandas.read_csv("./us-states-game-start/50_states.csv")

data_dict = data.to_dict()
print(data_dict)
