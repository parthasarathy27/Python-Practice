# import MyPackage.MyModule (or) from MyPackage import MyModule
# __init__.py
# __all__ = ["MyModule"]

# math package

import math

def cube(x):
    return x**3

a = int(input("Enter the Number : "))
print(f"a = {a}")
a = abs(a)
print(f"abs(a) = {a}")
print(f"Square Root of {a} =", math.sqrt(a))
print(f"Cube of {a} =", cube(a))

# Random Package

import random

b = int(input("Enter the Number : "))
for i in range(b):
    value = random.randint(1, 100)
    print(value)

# Globals(), Locals() AND Reload()
# reload(module_name)

import time
localtime = time.asctime(time.localtime(time.time()))
print(f"Local current time : {localtime}")

import calendar
print(calendar.month(2024, 9))

# Function Redefinition

import datetime
def showMessage(msg):
    print(msg)
showMessage("Hello")
def showMessage(msg):
    now = datetime.datetime.now()
    print(msg)
    print(str(now))
showMessage("Current Date and Time is : ")
