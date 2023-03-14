import pandas as pd

# Figuring out which names don't match in the two files.
# After this, went through and manually altered names.

# read the two csv files
data = pd.read_csv('data.csv')['Team'].unique()
names = pd.read_csv('MTeams.csv')['TeamName'].unique()

# convert to sets and find the difference
not_in_names = set(data) - set(names)

# print the names that are not in names.csv
print(list(not_in_names))

# Result
# ['Stephen F. Austin', 'Arizona St.', "Saint Mary's", 'Norfolk St.', 'College of Charleston', 'Georgia St.', 
# 'Green Bay', 'Loyola Chicago', 'Kansas St.', 'Little Rock', 'Appalachian St.', 'Boise St.', 'Wichita St.', 
# 'Colorado St.', 'New Mexico St.', 'St. Bonaventure', 'Eastern Washington', 'Montana St.', 'Fresno St.', 
# 'Jacksonville St.', 'Iowa St.', 'Coastal Carolina', 'Texas Southern', 'North Carolina Central', 
# 'Oklahoma St.', "Saint Joseph's", 'Southern', 'Weber St.', 'Texas A&M Corpus Chris', 'San Diego St.', 
# 'Prairie View A&M', 'Murray St.', 'Florida St.', 'Cal St. Bakersfield', 'Kent St.', 'Saint Louis',
#  'Fairleigh Dickinson', 'Morehead St.', 'Albany', "Saint Peter's", 'Oregon St.', 'Cleveland St.',
#  'North Carolina St.', 'Utah St.', 'North Dakota St.', "Mount St. Mary's", 'Northern Kentucky', 
# 'Michigan St.', 'South Dakota St.', 'Middle Tennessee', 'East Tennessee St.', 'Cal St. Fullerton', 'Wright St.', 'Mississippi St.', 'Ohio St.', "St. John's"]

# Second iteration
# ['Middle Tennessee', 'Southern', 'East Tennessee St.']