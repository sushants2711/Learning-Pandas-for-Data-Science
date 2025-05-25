# Learning rows and colums in a dataset frame and how to visualize it 

import pandas as pd

data = pd.read_json("sample_Data.json")

print(data)

# print first 10 rows from starting
print(data.head(10))

# print last 10 data frame from ending
print(data.tail(10))

#  by default if we not pass any value it will print first 5 value in head and last 5 value in tail

print("first 5 data from head")
print(data.head())

print("last 5 data of tail")
print(data.tail())