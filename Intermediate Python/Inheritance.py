# inheritance

# Multiple inheritance

# class Base1:
#   statement block
# class Base2:
#   statement block
# class Derived(Base1, Base2):
#   statement block

class Base1(object):
    def __init__(self):
        super(Base1, self).__init__()
        print("Base1 class")
class Base2(object):
    def __init__(self):
        super(Base2, self).__init__()
        print("Base2 class")
class Derived(Base1, Base2):
    def __int__(self):
        super(Derived, self).__init__()
        print("Derived class")
D = Derived()


# Multi-Level inheritance

# class Base:
#     pass
# class Derived1(Base):
#     pass
# class Derived2(Derived1):
#     pass

class Person:
    def name(self):
        print("Name...")
class Teacher(Person):
    def Qualification(self):
        print("Qualification...B.Tech")
class HOD(Teacher):
    def experience(self):
        print("Experience...at least 15 years")
        
hod = HOD()
hod.name()
hod.Qualification()
hod.experience()


# Multi-Path inheritance

class Student:
    def name(self):
        print('Name...')
class Academic_Performance(Student):
    def Acad_Score(self):
        print('Acadamic Score...65% and above')
class Engineer(Student):
    def Engineers(self):
        print('Engineering Score...60% and above')
class Result(Academic_Performance, Engineer):
    def Eligibility(self):
        print("*******Minimum Eligibility to Apply*******")
        self.Acad_Score()
        self.Engineers()

R = Result()
R.Eligibility()
