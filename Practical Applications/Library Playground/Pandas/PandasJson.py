# import the Json file

import pandas as pd

data = pd.read_json('demo.json')

print(data.to_string()) 

# using head() similar as csv

print(data.head(10))

# using tail() similar as csv

print(data.tail()) 

# using info() similar as csv

print(data.info()) 
