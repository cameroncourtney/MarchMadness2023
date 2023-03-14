import pandas as pd

# Read in the year.csv and year-p.csv files
year_df = pd.read_csv("data.csv", dtype={'Year': int}, thousands=',')
year_p_df = pd.read_csv('p-data.csv', dtype={'Year': int}, thousands=',')

# Merge the dataframes on the 'Team' column
merged_df = pd.merge(year_df, year_p_df[['Team', 'Year', 'Rk']], on=['Team', 'Year'], how='left')

# Rename columns after merge.
# Rk is the T-Rank of a team considering the entire season and confernce tournaments.
# P-Rk is the T-Rank of a team solely considering their conference tournament performance.
merged_df = merged_df.rename({'Rk_x': 'Rk', 'Rk_y': 'P-Rk'}, axis=1) 

# Export the final dataframe to a CSV file
merged_df.to_csv('final-data.csv', index=False)