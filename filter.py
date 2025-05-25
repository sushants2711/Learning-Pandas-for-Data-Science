
"""
1- select specific column 
2- filter rows
3- combine multiple conditions

1- square brackets
2- boolean conditions

selecting columns
1- a series
2- dataframe multiple colums of data

filtering rows
boolean indexing

column = df["column name"]
subset = df["column1", "column2", "...."]

based on single conditions
filtered_rows = df[df["column name"] > 8900]

combine multiple conditions
filtered_rows = df[(df["column name"] > 9000) & (df["column name"] >29)]

"""




import pandas as pd

data = {
    "Name": ["sushant", "riya", "diwakar", "anjali", "rishika", "akash", "kuldeep", "jaya", "chetan"],
    "Age": [19,21,34,21,22,21,12,34,43],
    "Salary": [45000,20000,40000,38000,21000,33000,89000,100000,38000],
    "Performance Score": [90,93,45,30,40,90,98,89,90]
}

df = pd.DataFrame(data)

# print(df)

# print("Names( single column return a series)")

# single data
name = df["Name"]
# print(name)

# selecting multiple data frame 
subset = df[["Name", "Salary", "Age"]]
# print(subset)

# filter on the basis of single condition
filter = df[df["Salary"] > 38000]
# print(filter)

filter2 = df[(df["Salary"] > 40000) & (df["Age"] < 32)]
# print(filter2)

# using or consitions
print("----")
filter3 = df[(df["Salary"] > 40000) | (df["Performance Score"] > 89)]
print(filter3)