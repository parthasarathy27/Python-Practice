# Python Writing files (.txt, .json, .csv)


employees = ["Professor", "Berlin", "Tokyo", "Rio"]

file_path = "D:/files/employees.txt"

try:
    with open(file = file_path, mode = "w") as file:
        for employee in employees:
            file.write(employee + "\t")
        print(f"txt file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")


'''
import json

employee = {
    "name": "Alvaro Morte",
    "age" : "35",
    "Job" : "Heist"
}

file_path = "D:/files/employeedata.json"

try:
    with open(file = file_path, mode = "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")
'''

'''
import csv

employees = [["Name", "Age", "Job"],
             ["Professor", "35", "Master"],
             ["Berlin", "42", "Asst Master"],
             ["Tokyo", "27", "Executor"]]

file_path = "D:/files/employees.csv"

try:
    with open(file = file_path, mode = "w") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")
'''