import csv
import numpy as np
import matplotlib.pyplot as plt


def analog_value(m, n):
    if m >= 128:
        return 0.005*((128-m)*256 - n)
    return 0.005*(m*256 + n)


with open("file.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    values = list(reader)
    values = np.array(values)

timeList = []
yawRateList = []
for myList in values:
    if myList[2] == "112":
        timeList.append(float(myList[0]))
        yawRateList.append(analog_value(int(myList[5]), int(myList[6])))

plt.plot(timeList, yawRateList)
plt.xlabel("Time")
plt.ylabel("Yaw Rate")
plt.show()
