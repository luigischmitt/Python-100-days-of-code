import pandas as pd

df = pd.read_csv("Python-100-days-of-code/day 25/2018_Central_Park_Squirrel_Census.csv")

data = df["Primary Fur Color"].value_counts()

data.to_csv("squirrel_count.csv")
