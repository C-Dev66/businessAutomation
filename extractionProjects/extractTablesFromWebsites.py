# This script will work on extrating tables from websites using the pandas pyton library
# In the past we have used Beautiful Soup

"""
To demo this script we will be using the folling website:
https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)

We will be pulling all of the tables found on this page using pandas
"""

import pandas as pd

# Use this command to read the html link, place the address into parantheses
# if you use (pd.read_) you can add a different tag to use an alternative source to pull information from

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')


print(len(simpsons))


# have to use the print command to see output onto terminal since we are not using Jupyter notebook
print(simpsons[1])











