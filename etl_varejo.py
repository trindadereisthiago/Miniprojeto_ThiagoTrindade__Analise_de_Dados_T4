import pandas as pd

path = ("Base Varejo.csv")

df = pd.read_csv(path, sep=";")

print(df)