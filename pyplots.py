# Author Raphael Wagner 23.08.2018

# import packages

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# definition of functions
def create_plot_arrays(data: object, stepsize: object, error: object, runtime: object, size: object) -> object:
    for i in range(size):
        stepsize[i] = np.log10(data[(i + 1) * 3 - 1])
        error[i] = data[(i + 1) * 3 - 3]
        runtime[i] = data[(i + 1) * 3 - 2]

    return 0


def exact(x):
    y = 1 - (1 - np.exp(-10)) * x - np.exp(-10 * x)
    return y


#################################################################
######################### MAIN PROGRAM ##########################
#################################################################

# read in files from cpp code

data_general = np.loadtxt("err_time_general_tridiagonal.txt")
data_optimized = np.loadtxt("err_time_optimized_solver.txt")
data_special = np.loadtxt("err_time_special_tridiagonal.txt")
data_lu = np.loadtxt("err_time_lu.txt")

results_10_general = np.loadtxt("results_general_tridiagonal10.txt")
results_100_general = np.loadtxt("results_general_tridiagonal100.txt")
results_1000_general = np.loadtxt("results_general_tridiagonal1000.txt")

results_10_optmized = np.loadtxt("results_optimized_solver10.txt")
results_100_optmized = np.loadtxt("results_optimized_solver100.txt")
results_1000_optmized = np.loadtxt("results_optimized_solver1000.txt")

results_10_special = np.loadtxt("results_special_tridiagonal10.txt")
results_100_special = np.loadtxt("results_special_tridiagonal100.txt")
results_1000_special = np.loadtxt("results_special_tridiagonal1000.txt")

results_10_lu = np.loadtxt("results_lu10.txt")
results_100_lu = np.loadtxt("results_lu100.txt")
results_1000_lu = np.loadtxt("results_lu1000.txt")
# length of arrays

size = int(len(data_general) / 3)
size_lu = 7

# create arrays

stepsize_general = np.zeros(shape=size)
error_general = np.zeros(shape=size)
runtime_genral = np.zeros(shape=size)

stepsize_optimized = np.zeros(shape=size)
error_optimized = np.zeros(shape=size)
runtime_optimized = np.zeros(shape=size)

stepsize_special = np.zeros(shape=size)
error_special = np.zeros(shape=size)
runtime_special = np.zeros(shape=size)

stepsize_lu = np.zeros(shape=size_lu)
error_lu = np.zeros(shape=size_lu)
runtime_lu = np.zeros(shape=size_lu)

y_excat = np.zeros(shape=1000)
x10 = np.zeros(shape=10)
x100 = np.zeros(shape=100)
x1000 = np.zeros(shape=1000)

# fill arrays

create_plot_arrays(data_general, stepsize_general, error_general, runtime_genral, size)
create_plot_arrays(data_lu, stepsize_lu, error_lu, runtime_lu, size_lu)
create_plot_arrays(data_special, stepsize_special, error_special, runtime_special, size)
create_plot_arrays(data_optimized, stepsize_optimized, error_optimized, runtime_optimized, size)

for i in range(10):
    x10[i] = (i + 1) / 11

for i in range(100):
    x100[i] = (i + 1) / 101

for i in range(1000):
    x1000[i] = (i + 1) / 1001
    y_excat[i] = exact((i + 1) / 1001)

# create plots

f, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(stepsize_general, runtime_genral, "blue", dashes=(5, 5))
ax1.plot(stepsize_special, runtime_special, "red", dashes=(4, 4))
ax1.plot(stepsize_optimized, runtime_optimized, "cyan", dashes=(2, 2))
ax1.plot(stepsize_lu, runtime_lu, "green", dashes=(3, 3))
ax1.set_ylabel("log10(runtime)")
ax1.set_xlabel("log10(stepsize)")
ax1.set_title("Runtime")

ax2.plot(stepsize_general, error_general, "blue", dashes=(5, 5))
ax2.plot(stepsize_special, error_special, "red", dashes=(4, 4))
ax2.plot(stepsize_optimized, error_optimized, "cyan", dashes=(2, 2))
ax2.plot(stepsize_lu, error_lu, "green", dashes=(3, 3))
ax2.set_ylabel("log10(error)")
ax2.set_xlabel("log10(stepsize)")
ax2.set_title("Error")

lu = mpatches.Patch(color='green', label='LU')
general = mpatches.Patch(color='blue', label='general')
special = mpatches.Patch(color='red', label='special')
optimized = mpatches.Patch(color='cyan', label='optimized')
plt.legend(handles=[lu, general, special, optimized])

plt.show()

d, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(x10, results_10_general, "blue", dashes=(5, 5))
ax1.plot(x10, results_10_optmized, "cyan", dashes=(2, 2))
ax1.plot(x10, results_10_special, "red", dashes=(4, 4))
ax1.plot(x10, results_10_lu, "green", dashes=(3, 3))
ax1.plot(x1000, y_excat, "orange", dashes=(2, 6))
ax1.set_xlabel("x")
ax1.set_ylabel("f(x)")
ax1.set_title("N=10")
lu = mpatches.Patch(color='green', label='LU')
general = mpatches.Patch(color='blue', label='general')
special = mpatches.Patch(color='red', label='special')
optimized = mpatches.Patch(color='cyan', label='optimized')
exact = mpatches.Patch(color='orange', label='exact')
plt.legend(handles=[lu, general, special, optimized])

ax2.plot(x100, results_100_general, "blue", dashes=(5, 5))
ax2.plot(x100, results_100_optmized, "cyan", dashes=(2, 2))
ax2.plot(x100, results_100_special, "red", dashes=(4, 4))
ax2.plot(x100, results_100_lu, "green", dashes=(3, 3))
ax2.plot(x1000, y_excat, "orange", dashes=(2, 6))
ax2.set_xlabel("x")
ax2.set_ylabel("f(x)")
ax2.set_title("N=100")

ax3.plot(x1000, results_1000_general, "blue", dashes=(5, 5))
ax3.plot(x1000, results_1000_optmized, "cyan", dashes=(2, 2))
ax3.plot(x1000, results_1000_special, "red", dashes=(4, 4))
ax3.plot(x1000, results_1000_lu, "green", dashes=(3, 3))
ax3.plot(x1000, y_excat, "orange", dashes=(2, 6))
ax3.set_xlabel("x")
ax3.set_ylabel("f(x)")
ax3.set_title("N=1000")

plt.show()
