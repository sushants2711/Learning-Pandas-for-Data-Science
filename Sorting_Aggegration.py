# sorting - based on the value in one or more data like alphabet sorting, ascending sorting, descending order

# sorting data in 1 coulmn sort_values()


import pandas as pd

data = {
    "Name": ["sushant", "riya", "diwakar", "anjali", "rishika", "akash", "kuldeep", "jaya", "chetan"],
    "Age": [19,21,34,21,22,21,12,34,43],
    "Salary": [45000,20000,40000,38000,21000,33000,89000,100000,38000],
    "Performance Score": [90,93,45,30,40,90,98,89,90]
}

data2 = {
    "Name": ["susha1", "riya1", "diwakar1", "anjali1", "rishika", "akash", "kuldeep", "jaya", "chetan"],
    "Age": [19,21,34,21,22,21,12,34,43],
    "Salary": [45000,20000,40000,38000,21000,33000,89000,100000,38000],
    "Performance Score": [90,93,45,30,40,90,98,89,90]
}
df = pd.DataFrame(data)
# print(df)

df1 = pd.DataFrame(data2)
print("----------")
print("Age as a ascending order ")

# only sorted for single coulmn 
# df.sort_values(by="Age", ascending=True, inplace=True)
# print(df)

# sorting multiple column 
# df.sort_values(by=["Age", "Salary"], ascending=[True, True], inplace=True)
# print(df)





# Aggregation 
"""
Aggregation involves finding sum, mean  and find summery Statics 

"""

meanis = df["Age"].mean()
print(meanis)

sumis = df["Age"].sum()
print(sumis)


# grouping in pandas
"""
syntax = df.groupby("col-name")["column- name"].sum().mean() - the 1st column represents selection group which solumn and second column represents what function perform in which column 
"""

group = df.groupby("Age")["Salary"].sum()
print(group)


# multiple column 
gp = df.groupby(["Age", "Name"])["Salary"].sum()
print(gp)

#  sum aggregation function
"""
1. sum()
2. mean()
3. count()
4. min()
5. min()
6. std()
"""

# merging data frames with two columns 
"""
join type = inner , outer, left, right and cross
"""

ab = pd.merge(df, df1, on="Name", how="inner")
print(ab)

print("--------")
print("--------")
print("--------")


# concate - it is a also a method to join all the column 
newdata = pd.concat([df, df1], axis=0, ignore_index=True)
print(newdata)
