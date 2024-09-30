import pandas as pd

df = pd.read_csv("AMSCelldata97.csv")
df.dropna(subset=["S1"], inplace=True) #removes empty rows
df["Average_Power"] = df["TSV"]*df["TSC"]
print(df["Average_Power"])
