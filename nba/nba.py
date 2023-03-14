import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'nbaFiles/nbaTeams.csv')

nba_dict = {"name":"name","abv":"abv"}
nba_dicts = []

urls = []


df = pd.read_csv(filename)
names = pd.DataFrame(df).iterrows()

x = 0

for i in names:
    nba_dict = {"name": i[1][0], "abv": i[1][1], "{}".format(i[1][1]):x}
    nba_dicts.append(nba_dict)
    x += 1

print(nba_dicts)

#Nba Players

#Nba Fun Facts