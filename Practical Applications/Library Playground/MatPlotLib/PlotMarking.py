import matplotlib.pyplot as plt
import numpy as np

point = np.array([4, 9, 2, 11])

# marker method

plt.plot(point, marker = 'D')
plt.show()

# color changing

plt.plot(point, 'o:g')
plt.show()

# marker size

plt.plot(point, marker = ',', ms = 20)
plt.show()

# markeredgecolor and markerfacecolor

plt.plot(point, marker = '*', ms = 20, mec = 'r', mfc = 'g')
plt.show()
