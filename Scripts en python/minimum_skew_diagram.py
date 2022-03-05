import numpy as np
import matplotlib.pyplot as plt

filename = "dataset_7_10.txt"
with open(filename, 'r') as file:
    data = file.read()

skew_array = np.array([0])

for i in range(1,len(data)+1):
    latest = len(skew_array)-1

    if(data[i-1]=="C"):
        val = -1
    elif(data[i-1]=="G"):
        val = 1
    else:
        val = 0
    skew_array = np.append(skew_array,skew_array[latest]+val)

min_skew = np.amin(skew_array)
index_skew = np.where(skew_array == min_skew)

for i in range(0,len(index_skew)):
    print(index_skew[i])

plt.plot(skew_array)
plt.show()