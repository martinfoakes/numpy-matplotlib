#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# fromFile() function can construct an array from data in a text or binary file
# using numpy arrays compared to normal python lists gives you the ability to
# use different types of number data types, they can store data as 8, 16 or 32 bits,
# you can use integers or floats, all the conversions and processing are handled by numpy internally
salaryValues = np.fromfile('./data-files/salaries.txt', dtype=int, sep=',')

# fromFile() does not handle strings so well, so will use the genfromtxt() function
# This function allows you to load data from a text file, with slightly different parameter names
namesValues = np.genfromtxt('./data-files/names.txt', dtype='str', delimiter=',')

# Now just need to plot the names vs the salaries

x = np.arange(len(namesValues))

plt.bar(x, salaryValues)

plt.xticks(x, namesValues)

plt.ylabel("Salaries")
plt.xlabel("Names")
plt.title("Salary of 10 random people")

# print out the max, min, average, and median amounts for salaries.txt
print('Max salary is:', np.max(salaryValues), 'Min salary is:', np.min(salaryValues), 'Average salary is:', np.average(salaryValues), 'Median salary is:', np.median(salaryValues))

# Then display the plot
plt.show()

# As the top and bottom values are so high/low, the bar graph is hard to read due to the extremes
# To fix this you can get rid of the upper and lower two values in the data
# Removing the extreme values that may be interfering with the results

# Remove the top and bottom two entries of the arrays
salaries_new = salaryValues[2:-2]
names_new = namesValues[2:-2]

z = range(len(names_new))

plt.bar(z, salaries_new)
plt.xticks(z, names_new)
plt.show()