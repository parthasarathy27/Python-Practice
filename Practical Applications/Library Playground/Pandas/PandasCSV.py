# using csv file

import pandas as pd

data = pd.read_csv('demo.csv')

print(data.to_string())

# maximum rows

print(pd.options.display.max_rows)

# display the entire DataFrame

pd.options.display.max_rows = 9999

data = pd.read_csv('data.csv')

print(data) 

# same as json data = pd.read_json('demo.json')

# finding Duplicate

print(data.duplicated())

# removing duplicate

data.drop_duplicates(inplace = True)
print(data)
