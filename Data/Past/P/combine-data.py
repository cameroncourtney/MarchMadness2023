import pandas as pd
import glob

# Define a list of file names in the "All" folder
files = glob.glob("./*.csv")

# Create an empty list to hold the dataframes for each file
dfs = []

# Loop through the files and read each one into a dataframe
for file in files:
    year = file.split("-")[0][-4:] # Extract the year from the file name
    df = pd.read_csv(file, usecols=["Rk", "Team", "Adj OE", "Adj DE", "Barthag", "Record", "Wins", "Games", "eFG", "eFG D.", "FT Rate", "FT Rate D", "TOV%", "TOV% D", "O Reb%", "Op OReb%", "Raw T", "2P %", "2P % D.", "3P %", "3P % D.", "Blk %", "Blked %", "Ast %", "Op Ast %", "3P Rate", "3P Rate D", "Adj. T", "Avg Hgt.", "Eff. Hgt.", "Exp.", "PAKE", "PASE", "Talent", "FT%", "Op. FT%", "PPP Off.", "PPP Def.", "Elite SOS"])
    df.drop('Year', axis=1)
    df['Year'] = int(year) # Add a new column for the year
    df['Year'] = df['Year'].astype(int) 
    dfs.append(df)

# Concatenate all the dataframes together
result = pd.concat(dfs, ignore_index=True)

# Export the final dataframe to a CSV file
result.to_csv("../Combine/p-data.csv", index=False)
print("Combined CSV file saved to Combine/p-data.csv")