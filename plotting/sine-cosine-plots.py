#!/usr/bin/python

import numpy as np
# matplotlib is a HUGE library, only import the thing you need
import matplotlib.pyplot as plt

# Using the numpy linspace() function you can generate evenly spaced out values
x = np.linspace(0, 20, 1000)
# In this example linspace() will generate 1000 evenly spaced out values between 0 and 20

# Calculate the sin and cos values for the array of spaced values [x]
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the sin and cos functions using pyplot
plt.plot(x, y1, '-g', label='sine')
plt.plot(x, y2, '-b', label='cos')
# First two arguments are X and Y axis
# Third argument is the color: -g green, -b blue
# Last is the label that shows up in a legend for the plot
# Can set the position of the legend using:
plt.legend(loc="upper right")

# Limit the y axis to -1.5 to 1.5 to give the graph better readability
plt.ylim(-1.5, 1.5)
plt.show()