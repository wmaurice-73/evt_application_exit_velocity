import pandas as pd
import numpy as np

#This file combines and smoothes the raw data from 2015 - 2025 to a dataframe called df_25_sorted

#For every season we import the data available for every player who had at least 1 BBE (Batted Ball Event) in the first step
#In the second step we reduce the raw data to a dataframe that only contains player information and the Maximum Exit Velocity achieved in that season
df_2025_raw = pd.read_csv("./data/raw/exit_velocity_2025.csv")
df_2025 = df_2025_raw[["player_id","max_hit_speed"]]

df_2024_raw = pd.read_csv("./data/raw/exit_velocity_2024.csv")
df_2024 = df_2024_raw[["player_id","max_hit_speed"]]

df_2023_raw = pd.read_csv("./data/raw/exit_velocity_2023.csv")
df_2023 = df_2023_raw[["player_id","max_hit_speed"]]

df_2022_raw = pd.read_csv("./data/raw/exit_velocity_2022.csv")
df_2022 = df_2022_raw[["player_id","max_hit_speed"]]

df_2021_raw = pd.read_csv("./data/raw/exit_velocity_2021.csv")
df_2021 = df_2021_raw[["player_id","max_hit_speed"]]

df_2020_raw = pd.read_csv("./data/raw/exit_velocity_2020.csv")
df_2020 = df_2020_raw[["player_id","max_hit_speed"]]

df_2019_raw = pd.read_csv("./data/raw/exit_velocity_2019.csv")
df_2019 = df_2019_raw[["player_id","max_hit_speed"]]

df_2018_raw = pd.read_csv("./data/raw/exit_velocity_2018.csv")
df_2018 = df_2018_raw[["player_id","max_hit_speed"]]

df_2017_raw = pd.read_csv("./data/raw/exit_velocity_2017.csv")
df_2017 = df_2017_raw[["player_id","max_hit_speed"]]

df_2016_raw = pd.read_csv("./data/raw/exit_velocity_2016.csv")
df_2016 = df_2016_raw[["player_id","max_hit_speed"]]

df_2015_raw = pd.read_csv("./data/raw/exit_velocity_2015.csv")
df_2015 = df_2015_raw[["player_id","max_hit_speed"]]

#Combine all the data from 2015 - 2025 to a single dataframe
df_15_25 = pd.concat([df_2015,df_2016,df_2017,df_2018,df_2019,df_2020,df_2021,df_2022,df_2023,df_2024,df_2025], ignore_index=True)

#drop every entry where no max hit speed has been reported 
df_combined = df_15_25.dropna(subset=["max_hit_speed"])

#We only keep the personal best of every player
df_25_max = (df_combined.groupby("player_id", as_index=False)["max_hit_speed"].max())

#Drop the column containing the players-ids
df_25 = df_25_max[["max_hit_speed"]]

#sorted dataframe (corresponds to order statistics X_1,n \leq ... \leq X_n,n)
df_25_sorted = df_25.sort_values(["max_hit_speed"],ascending=True)

#collect every entry appearing in the data
entries = np.unique(df_25_sorted["max_hit_speed"])

#smoothen the data according to the procedure presented in Chapter 6
for val in entries:
    idx = np.where(df_25_sorted["max_hit_speed"] == val)
    m = len(idx[0])
    if m>1:
        for j in range(m):
            df_25_sorted.iloc[idx[0][j]] = val - 0.05 + 0.1*((2*(j+1)-1)/(2*m))

#uncomment the next to lines to save the data as a csv to use for further application in python or R
#we have already done this, you can find the processed data in the data -> processed folder
#df_25_sorted.to_csv("./data/processed/ev_combined_python.csv", index=False)
#df_25_sorted.to_csv("./data/processed/ev_combined_R.csv", index=False, sep=";", decimal=",")