import numpy as np

# Dimensions in Arrays

col  = np.array(45)
col1 = np.array([1, 2, 3, 4])
col2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
col3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],[[9, 0, 1, 2], [3, 4, 5, 6]]])

print(f"0-D Arrays:\n{col}\n")
print(f"1-D Arrays:\n{col1}\n")
print(f"2-D Arrays:\n{col2}\n")
print(f"3-D Arrays:\n{col3}\n")

# Check Number of Dimensions

print(f'number of dimensions - 0 :{col.ndim}')
print(f'number of dimensions - 1 :{col1.ndim}')
print(f'number of dimensions - 2 :{col2.ndim}')
print(f'number of dimensions - 3 :{col3.ndim}')

# Array Indexing

print('Add two rows :', col2[0] + col2[1])
print('2nd element on 1st row:', col2[0, 1])
print('5th element on 2nd row:', col2[1, 4])
print('the third element of the second array of the first array :', col3[0, 1, 2])
print('Last element from 2nd dim: ', col2[1, -1])
