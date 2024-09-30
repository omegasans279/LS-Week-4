
import csv
import numpy as np
import matplotlib.pyplot as plt


def analog_value(m, n):
    if m >= 128:
        return 0.0001274 * ((128 - m) * 256 - n)
    return 0.0001274 * (m * 256 + n)


with open("file.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    values = list(reader)
    values = np.array(values)

timeList = []
accXList = []
for myList in values:
    if myList[2] == "128":
        timeList.append(float(myList[0]))
        accXList.append(analog_value(int(myList[9]), int(myList[10])))

plt.plot(timeList, accXList)
plt.xlabel("Time")
plt.ylabel("Acc X-axis")
plt.show()
