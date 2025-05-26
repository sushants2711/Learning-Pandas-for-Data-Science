# update the column value

import pandas as pd

data = {
    "Name": ["sushant", "riya", "diwakar", "anjali", "rishika", "akash", "kuldeep", "jaya", "chetan"],
    "Age": [19,21,34,21,22,21,12,34,43],
    "Salary": [45000,20000,40000,38000,21000,33000,89000,100000,38000],
    "Performance Score": [90,93,45,30,40,90,98,89,90]
}

df = pd.DataFrame(data)
print(df)

print("Modified data \n")

# delete single column
df.drop(columns=["Age"], inplace=True)
print(df)

# to delete multiple column
df.drop(columns=["Name","Salary"], inplace=True)
print(df)

# to delete a entire single row of each column
df.drop(index=0, inplace=True)
print(df)