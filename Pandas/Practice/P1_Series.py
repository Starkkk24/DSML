import pandas as pd
import numpy as np

# Creating pd Series

p = pd.Series([1,2,3,4,5], index=["A", "B", "C", "D", "E"])
n = np.array([1,2,3,4,5])
print(f"NumPy: {type(n)}\n{n}\n")
print(f"Pandas: {type(p)}\n{p}")
