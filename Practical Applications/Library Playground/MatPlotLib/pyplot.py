# matplotlib

# pyplot method

import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([0, 10])
ypoint = np.array([0, 250])

plt.plot(xpoint, ypoint)
plt.show()

# string notation parameter 'o'

xpoint = np.array([0, 10])
ypoint = np.array([0, 50])

plt.plot(xpoint, ypoint, 'o')
plt.show()

# Line in a diagram

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# leave out the x-points

zpoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(zpoints)
plt.show()
