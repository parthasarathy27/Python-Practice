# Class and Object
# class_name:
# object_name = class_name()
# object_name.class_member_name

class laptop:
    price = 0
    procs = ""
    ram   = ""

hp = laptop()
dell = laptop()

hp.price = 50000
hp.procs = "i5"
hp.ram   = "8GB"

dell.price = 60000
dell.procs = "i7"
dell.ram   = "16GB"

print("Hp Laptop\n")
print(f"Hp price : {hp.price}\nHp procs : {hp.procs}\nHp ram   : {hp.ram}\n")
print("Dell Laptop\n")
print(f"Dell price : {dell.price}\nDell procs : {dell.procs}\nDell ram   : {dell.ram}")

# odd or even using class method

class number:
    even = []
    odd = []
    def __init__(self, num):
        self.num = num
        if num % 2 == 0:
            number.even.append(num)
        else:
            number.odd.append(num)

N1 = number(21)
N2 = number(32)
N3 = number(43)
N4 = number(54)
N5 = number(65)

print(f"Even Number are : {number.even}")
print(f"Odd Number are : {number.odd}")
