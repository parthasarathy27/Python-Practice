# fileObj = open(filename [, access_mode])

import fileinput

# write() Method

file = open("text.txt", "w")
file.write("Welcome to Python World")
file.close()
print("Data Written into the file....")

# writelines() Method

file = open("text.txt", "w")
lines = ["Hello World, ", "Welcome to the world of python"]
file.writelines(lines)
file.close()
print("Data written to file...")
