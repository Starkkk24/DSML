import pandas as pd

# Exploratory Data Analysis
dat = pd.read_csv("edata.csv")

print(f"Data:\n{dat}")
print(f"\nHead:\n{dat.head()}")
print(f"\nTail:\n{dat.tail()}")
print(f"\nColumn Structure:\n{dat.info()}")
print(f"\nStats:\n{dat.describe()}")
print(f"\nShape:\n{dat.shape}")