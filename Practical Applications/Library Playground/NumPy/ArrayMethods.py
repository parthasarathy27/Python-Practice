# copy and View

# copy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(f"Make a copy : {x}")

# view

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(f"Make a view : {x}")

# shape and Reshape

# shape

import numpy as np

arr1 = np.array(["hp", "Dell", "lenovo", "mac"], ndmin=5)
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr1)
print('shape of array :', arr1.shape)
print(arr2.shape)

# Reshape

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = arr1.reshape(-1)
y = arr2.reshape(2, 2, -1)

print(x)
print(y)

# iteration

import numpy as np

arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
arr3 = np.array([1, 2, 3])

for x in arr1:
    for y in x:
        for z in y:
            print(f"Using For loop method : {z}")

for x in np.nditer(arr2):
    print(f"Using nditer method : {x}")

for idx, x in np.ndenumerate(arr3):
    print("Using ndenumerate method:",idx, x)
