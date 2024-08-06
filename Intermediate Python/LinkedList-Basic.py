# Linked Lisr # Node

# class {className}:

'''
class AdmissionForm:

    Name = None
    Age = None
    Gender = None
    Address = None

    def __init__(self, Name, Age, Gender, Address):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Address = Address

xerox1 = AdmissionForm("John Wick", 22, "Male", "Texas")

xerox2 = AdmissionForm("Walter White", 34, "Male", "Mexico")

print(xerox1)
'''

# Simple Example for Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.pointer = None

head = Node(1)
node2 = Node(2)
node3 = Node(3)

head.pointer = node2
node2.pointer = node3

cur = head

while (cur is not None):
    print(cur.data)
    cur = cur.pointer
