# System Module

import sys
print("\n PYTHONPATH = \n", sys.path)

# Math Module

from math import pi, sqrt as square_root
print("PI = ", pi)
print("Sqrt = ", square_root(81))

# Name of the Module

print("Hello")
print("Name of this module is : ", __name__)

# Use a Module

def display():
    print("Hello")
    print("Name of this module is : ", __name__)
str = "Welcome to the world of Python !!!"

import MyModule
print("MyModule str = ", MyModule.str)
MyModule.display()
print("Name of calling module is : ", __name__)

# Variable in module

def large(a, b):
    if (a > b):
        return a
    else:
        return b
import MyModule
print("large (50, 100) = ", MyModule.large(50, 100))
print("large ('B', 'C') = ", MyModule.large('B', 'C'))
print("large('HI', 'BI')", MyModule.large('HI', 'BI'))

# dir() Fuction

def print_var(x):
    print(x)
x = int(input())
print_var(x)
print(dir())
