# Python reading files (.txt, .json, .csv)


'''
file_path = "D:/files/employees.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
    print(content)

except FileNotFoundError:
    print("That file was not found!")

except PermissionError:
    print("You do not have permission to read that file")
'''

'''
import json

file_path = "D:/files/employeedata.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
    print(content["name"])

except FileNotFoundError:
    print("That file was not found!")

except PermissionError:
    print("You do not have permission to read that file")
'''

import csv

file_path = "D:/files/employees.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])

except FileNotFoundError:
    print("That file was not found!")

except PermissionError:
    print("You do not have permission to read that file")