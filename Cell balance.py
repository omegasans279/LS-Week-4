import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AMSCelldata97.csv")

timeList = []
for i in range(df.shape[0]):
    timeList.append((i+1)/10)

for i in range(6):
    df["mean " + str(i+1)] = df.iloc[:, (15*i):(15*i+14)].mean(axis=1)
df["mean 7"] = df.iloc[:, 90:95].mean(axis=1)

plt.plot(timeList, df.iloc[:, 1000:1007])
plt.show()
