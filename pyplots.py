# Author Raphael Wagner 23.08.2018

# import packages

import numpy as np
import matplotlib.pyplot as plt

# definition of functions




# read in files from cpp code

data_general = np.loadtxt("err_time_general_tridiagonal.txt")
data_lu = np.loadtxt("err_time_lu")


# length of arrays

size = int(len(data_general) / 3)
size_lu = 7

points = np.zeros(shape=size)
error = np.zeros(shape=size)
runtime = np.zeros(shape=size)

for i in range(size):
    points[i] = np.log10(data_general[(i + 1) * 3 - 1])
    error[i] = data_general[(i + 1) * 3 - 3]
    runtime[i] = data_general[(i + 1) * 3 - 2]

print(points)
print()
print(error)
print()
print(runtime)

# generate plots test

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(points, runtime)
ax1.set_ylabel("log10(runtime)")
ax1.set_xlabel("log10(gridpoints)")

ax2.plot(points, error)
ax2.set_ylabel("log10(error)")
ax2.set_xlabel("log10(gridpoints)")

plt.show()
