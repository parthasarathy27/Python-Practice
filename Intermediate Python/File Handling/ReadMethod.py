# fileObj = open(filename [, access_mode])
import fileinput

# The read() Method

file = open("text.txt", "r")
print(file.read(11))
file.close()

# readline() Method

file = open("text.txt", "r")
print(file.readlines())
file.close()

# list Method

file = open("text.txt", "r")
print(list(file))
file.close()

# For loop Method

file = open("text.txt", "r")
for line in file:
    print(line)
file.close()
