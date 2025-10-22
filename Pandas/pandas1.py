import pandas as pd

dat = pd.Series([1,2,3,4,5,6], index=["A","B","C","D","E","F"])
# print(dat)


data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}
 

# Read into pandas from dictionary
datt = pd.DataFrame(data, index=["A","B","C"])
# print(datt)

# Read a CSV file and an Excel file
xl = pd.read_csv("datfile.csv")
print(xl)
# xl.info()
# print(xl.describe())
# print(xl.head())
# print(xl.tail())

#  Read a JSON file
jsn = pd.read_json("data2.json")
# print(jsn)

# Read a CSV file through a URL

# Read a sqlite3 file or SQL

