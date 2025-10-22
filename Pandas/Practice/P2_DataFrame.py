import pandas as pd
import numpy as np
import json

# Reading a CSV file as pd
dat = pd.read_csv("edata.csv")
# print(dat)


# Reading a python object as pd Dataframes
p2 = {
        "id": [1,2,3,4], 
        "name": ["Amit", "Priya", "Rahul", "Sara"], 
        "friends": [2, 3 ,6, 9],
        "liked_pages": [102, 101, 104, 109]
    }
pf = pd.DataFrame(p2)
# print(pf)


# Creating a python list in to pd Dataframe 
p3 = [
    ["Alice", 25],
 ["Bob", 30],
 ["Charlie", 35]
]
pff = pd.DataFrame(p3, columns=["Name", "Age"])
# print(pff)


#  Creating a numpy array into pd Dataframe
p4 = np.array([[1,2,4,3,5],[7,0,9,8,10]])
pfff = pd.DataFrame(p4, index=["->","->"], columns=["A","B","C","D","E"])
# print(pfff)


