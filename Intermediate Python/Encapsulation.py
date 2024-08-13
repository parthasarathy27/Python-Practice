# Encapsulation Concept

class Student:
    def __init__(self, name, rollno, age):
        self.name = name       # public instance variable
        self._rollno = rollno  # protectded instance variable
        self.__age = age       # private instance variable
    def __display(self):
        print(f"Hi, I am {self.name}, {self.__age} years old, with roll number {self._rollno} from the Student class.")
    def displayPrivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        print(f"My rollNo is {self._rollno}")

# calling protected data
def showData():
    b1 = Branch("Nisha", 1001)
    print(b1.name)
    print(b1._rollno)

# calling private data
showData()
s1 = Student("Rahul", 1002, 20)
print(s1._Student__age)
s1._Student__age = 45
s1._Student__display()

#another method to calling private data
s1.displayPrivateData()
print(s1.name)
s1.display()

# using get and set method in Encapsulation

class Student:
    def __init__(self, name, rollno, age):
        self.name = name       # public instance variable
        self._rollno = rollno  # protectded instance variable
        self.__age = age       # private instance variable

    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 35:
            print("Invalid age given...Age should be less than 35.")
        else:
            self.__age = age


s1 = Student("Rahul", 1002, 20)
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())
