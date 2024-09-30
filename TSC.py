import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("AMSCelldata97.csv")
timeList = []
for i in range(df.shape[0]):
    timeList.append((i+1)/10)
  
TSC = df["TSC"]
plt.plot(timeList, TSC)
plt.show()
