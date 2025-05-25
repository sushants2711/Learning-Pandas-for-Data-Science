import pandas as pd

data = pd.read_json("sample_Data.json")

print(data)

print(data.shape)
print(data.columns)