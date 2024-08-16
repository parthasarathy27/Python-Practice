import pandas as pd

# pandas import Process

# using DataFrame Function

Student = {
    'Student' : ["Ram", "John", "Ravi", "Jothi"],
    'Department' : ['CSE', 'ECE', 'MECH', 'CSE'],
    'Percentage' : [78, 89, 68, 75]
}

result = pd.DataFrame(Student)

print(result)
print(result.loc[[0, 2]])

# using Series Function

Duration = {'day1' : 410, 'day2' : 340, 'day3' : 230}

calories = pd.Series(Duration, index = ['day1', 'day2'])

print(calories)
