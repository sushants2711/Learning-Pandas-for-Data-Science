# adding new column in datasets

import pandas as pd

data = {
    "Name": ["sushant", "riya", "diwakar", "anjali", "rishika", "akash", "kuldeep", "jaya", "chetan"],
    "Age": [19,21,34,21,22,21,12,34,43],
    "Salary": [45000,20000,40000,38000,21000,33000,89000,100000,38000],
    "Performance Score": [90,93,45,30,40,90,98,89,90]
}

df = pd.DataFrame(data)

# print(df)

# I want to add one new column in a dataset also 

df["Bonus"] = (df["Salary"] * 20) / 100
print(df)
