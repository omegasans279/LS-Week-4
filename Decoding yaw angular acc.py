import csv
import numpy as np
import matplotlib.pyplot as plt


def analog_value(m, n):
    if m >= 128:
        return 0.125 * ((128 - m) * 256 - n)
    return 0.125 * (m * 256 + n)


with open("file.csv", 'r', newline='') as file:
    reader = csv.reader(file)
    values = list(reader)
    values = np.array(values)

timeList = []
yawAngList = []
for myList in values:
    if myList[2] == "128":
        timeList.append(float(myList[0]))
        yawAngList.append(analog_value(int(myList[5]), int(myList[6])))

plt.plot(timeList, yawAngList)
plt.xlabel("Time")
plt.ylabel("Yaw Angular Acc")
plt.show()
