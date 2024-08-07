# fileObj = open(filename [, access_mode])

import fileinput

# append() Method

file = open("text.txt", "a")
file.write("\nPyhton is a very simple yet powerful language")
file.close()
print("Data appended to file....")
