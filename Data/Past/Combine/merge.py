import pandas as pd

# Read in the year.csv and year-p.csv files
year_df = pd.read_csv("data.csv", dtype={'Year': int}, thousands=',')
year_p_df = pd.read_csv('p-data.csv', dtype={'Year': int}, thousands=',')

# Merge the dataframes on the 'Team' column
merged_df = pd.merge(year_df, year_p_df[['Team', 'Year', 'Rk']], on=['Team', 'Year'], how='left')

# Export the final dataframe to a CSV file
merged_df.to_csv('final-data.csv', index=False)