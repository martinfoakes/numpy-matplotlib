#!/usr/bin/python

# LIST COMPREHENSIONS
import numpy as np

# Before List Comprehensions was a thing, the old way to work with lists,
# doing something to them and returning a new list, was handled by looping over the list, like so:
x = [5, 10, 15, 20, 25]

y = []

for counter in x:
  y.append(counter / 5)

# the format() command allows you to send values to be printed inside the curly brackets {}
print('This is how it was done with loops: x = {} y = {}'.format(x, y))
# Output: 'This is how it was done with loops: x = [5, 10, 15, 20, 25] y = [1, 2, 3, 4, 5]'

# But NOW, there is an easier way to work with lists called List Comprehension
# Rather than having to loop all the time

# The format of List Comprehension is as follows:
# [ <do something> for value in list ]

# So for our example using array x divided by 5 ->
z = [n/5 for n in x]

print('Done using list comprehensions, output is: x = {} z = {} \n'.format(x, z))

# If you try to just divide [x] directly by 5 (a = x / 5), you will return an error
# BUT, you CAN directly divide [x] by 5 using NUMPY arrays
# For example:

# Convert [x] to a numpy array
a = np.array(x)
b = a / 5
print('Using a numpy array division, output is: a = {} b = {} \n'.format(a, b))