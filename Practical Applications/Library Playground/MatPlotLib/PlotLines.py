import matplotlib.pyplot as plt
import numpy as np

point = np.array([4, 9, 2, 11])

# linestyle method

plt.plot(point, linestyle = 'dotted')  # ls = 'dashed'
plt.show()

# line color

plt.plot(point, c = 'y') # color = 'hotpink' or '#4CAF50'
plt.show()

# line width

plt.plot(point, linewidth = '20')
plt.show()

# Multiple lines

First = np.array([3, 8, 1, 10])
Last = np.array([6, 2, 7, 11])

plt.plot(First)
plt.plot(Last)

plt.show()

# single function

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
x1 = np.array([0, 1, 2, 3])
y1 = np.array([6, 2, 7, 11])

plt.plot(x, y, x1, y1)
plt.show()
