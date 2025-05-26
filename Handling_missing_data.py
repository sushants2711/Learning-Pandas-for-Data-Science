# NaN - not a number
# None - for object data types

# isnull() - is the function through which we should check the value is null or not, it only returns boolean value either it should be True or False

import pandas as pd

data = {
    "Name": ["sushant", None, "diwakar", "anjali", "rishika", "akash", "kuldeep", "jaya", "chetan"],
    "Age": [19, None, 34,21,22,21,12,34,43],
    "Salary": [45000,None ,40000,38000,21000,33000,89000,100000,38000],
    "Performance Score": [90,None,45,30,40,90,98,89,90]
}

df = pd.DataFrame(data)

# print(df)

check_isNull = df.isnull() # to find the null values

# print(check_isNull) 

# print(df.isnull().sum())  # it gives you sum of each coulmns of missing value 

# print(df.isnull().sum().sum()) # it gives you total null values


# delete the missing value
# df.dropna(axis=0, inplace=True)
# print(df)

# fill the missing value 
# syntax -- .fillna(value, inplace = True)

# df.fillna(0, inplace=True)
# print(df)

# df["Age"].fillna(df["Age"].mean(), inplace=True)
# print(df)

# df["Salary"].fillna(df["Salary"].mean(), inplace=True)
# print(df)

# create a object and fill all the value 
# df.fillna({
#     "Age": df["Age"].mean(),
#     "Salary": df["Salary"].mean(),
#     "Performance Score": df["Performance Score"].mean()
# }, inplace=True)

# print(df)

# Interpolation - It is a technique in which we can fill the estimate missing value, and work only in integers .
# 1- preserve data intergrity
# 2- smooth trends to find 
# 3- consistency 
# 4- avoid data loss

# Linear, polynomial, time -- must study for data science at least when you are begineer 
df["Age"].interpolate(method="linear", inplace=True) # it is useful when you are working with a series and time frame data
print(df)

# 1- time series data 
# 2- numeric data when it is trends
# advamtages 
# database must be structured,
# estimate value fill it 

# disadvantages
#  It always not fill exactly like that happens 



#  bfill and ffill are also two methods that are use for fill the data also 

