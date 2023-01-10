import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image

def fit_line(x_fit, y_fit):
    x_array = np.array(x_fit)
    y_array = np.array(y_fit)
    a, b = np.polyfit(x_array, y_array, 1)
    return a, b, x_array

files = os.listdir("plots\midterm\msds\\")

# print(files)

coeffs = []

for i in files:
    msd = pd.DataFrame(np.loadtxt("plots\midterm\msds" + "\\" + i))
    # print(msd)

    msd_sliced_x = msd[0][18:]
    msd_sliced_y = msd[1][18:]

    a_fit, b_fit, x_fit = fit_line(msd_sliced_x, msd_sliced_y) # fit the line
    # plt.plot(x_fit, a_fit*x_fit+b_fit, color = 'tab:red', linewidth=0.5) # plot the fitted line

    coeffs.append(a_fit)

# print(coeffs)

#-----------------------------------------------------------------------------------------------------------------

print("start")

files2 = os.listdir("plots\midterm\msds_15\\")

coeffs2 = []

for j in files2:
    msd_15 = pd.DataFrame(np.loadtxt("plots\midterm\msds_15" + "\\" + j))
    # print(msd)

    msd_15_sliced_x = msd_15[0][18:]
    msd_15_sliced_y = msd_15[1][18:]

    a_fit, b_fit, x_fit = fit_line(msd_15_sliced_x, msd_15_sliced_y) # fit the line
    # plt.plot(x_fit, a_fit*x_fit+b_fit, color = 'tab:red', linewidth=0.5) # plot the fitted line

    coeffs2.append(a_fit)

print(coeffs2)