# Add the Elements of Two Lists

# Using Zip(x, y) method

x = [2, 4, 6, 7]
y = [3, 5, 7, 8]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)

# using add(x, y) Method

import numpy as np

x = [1, 3, 5, 7]
y = [2, 4, 6, 8]

z = np.add(x, y)
print(z)
