import pandas as pd

# read the two csv files
data = pd.read_csv('data.csv')['Team'].unique()
names = pd.read_csv('MTeams.csv')['TeamName'].unique()

# convert to sets and find the difference
not_in_names = set(data) - set(names)

# print the names that are not in names.csv
print(list(not_in_names))