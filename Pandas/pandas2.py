import pandas as pd

xl = pd.read_csv("datfile.csv")
# print(xl)

# print(xl[['Name', 'Marks']])
# print(xl.loc[1])
# print(xl.iloc[1])
# print(xl.iloc[1,0])

# print(xl.iloc[0:14:2,0:4])

# print(xl.at[1,'Name'])
# print(xl.iat[1,0])
# print(xl[(xl['Age']>18) & (xl['Marks']>50)])
print(xl.query("Age == 23 and 90>Marks >=75"))
# print(xl[xl['Age']<18])
