# This project will work on extracting CSV files from websites
# Using Pandas


# The source url will be
# https://www.football-data.co.uk/data.php

"""

Description: This python scrip will be to used scrape a website for CSV files.
Instead of manually downloading each csv file, we will create a pandas method that will
read each file. By using a for loop we can automate this and download all the files listed
instead of clicking one by one.


"""
import pandas as pd

# reading 1 csv file from the website
df_premier21 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

print(df_premier21)

# Renaming some of the columns to get a better understanding

df_premier21.rename(columns={'FTHG':'home_goals', 'FTAG':'away_goals'}, inplace=True)

print(df_premier21)
