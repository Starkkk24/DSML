import pandas as pd

p = pd.read_csv("edata.csv")
print(p)
print("\n")
# print(f"{p[["ID", "Name"]]}")

print(p.loc[0:4, ["Name", "Salary"]])
print("\n")
print(p.iloc[0:5, [1,4]])
print("\n")
print(p.at[0, "Name"])
print("\n")
print(p[p["Experience"]>=4])