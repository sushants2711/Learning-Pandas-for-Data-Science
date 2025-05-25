import pandas as pd

data = {
    "Name": ["Sushant", "Diwakar", "Jaya", "Rishika"],
    "Age": [20,22,23,21],
    "City": ["Chandigarh", "Delhi", "Jalandhar", "Mumbai"]
}

df = pd.DataFrame(data)

print(df)

# save the file after data mainpulation, cleaning , deleting etc
# df.to_csv("output2.csv", index=False)
# df.to_excel("output2.xlsx", index=False)
# df.to_json("output2.json", index=False)