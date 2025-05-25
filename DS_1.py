import pandas as pd

# pip3 install pandas   
# pip3 install xlrd
# pip3 install openpyxl

# read the fiels 
# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# df = pd.read_excel("SampleSuperstore.xlsx")
df = pd.read_json("sample_Data.json")
print(df)
