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

# frompyfunc Method

import numpy as np

def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# simple arithmetic problems

import numpy as np


arr1 = np.array([22, 27, 25, 20, 29, 30])
arr2 = np.array([10, 11, 12, 13, 14, 15])

result1 = np.add(arr1, arr2)
result2 = np.subtract(arr1, arr2)
result3 = np.multiply(arr1, arr2)
result4 = np.divide(arr1, arr2)
result5 = np.remainder(arr1, arr2)
result6 = np.mod(arr1, arr2)

print(f'Addition operation : {result1}')
print(f'Subtract operation : {result2}')
print(f'Multiply operation : {result3}')
print(f'Divition operation : {result4}')
print(f'Remainder operation : {result5}')
print(f'modulus operation : {result6}')
