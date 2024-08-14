from numpy import random

numbers1 = random.randint(10)
numbers2 = random.rand()
numbers3 = random.randint(50, size=(3, 5))
numbers4 = random.choice([2, 4, 6, 8, 10], size = (3, 5))

print(numbers1)
print(numbers2)
print(numbers3)
print(numbers4)

# Data Distribution

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
y = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)
print(y)

# Random Permutation

import numpy as np

arr = np.array([1, 3, 5, 7, 9])

random.shuffle(arr)

print(arr)

print(random.permutation(arr))
