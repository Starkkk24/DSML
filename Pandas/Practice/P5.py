import pandas as pd

p = pd.read_csv("edata.csv")
# print(p)

# print(p.isnull().sum())

p["Worth"] = p["Salary"].apply(lambda x : "Rich :)" if x >50000 else "Poor :(")
print(p)