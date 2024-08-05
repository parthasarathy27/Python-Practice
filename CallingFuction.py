# invoice Example:

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

username = input("Enter the username : ")
amount = float(input("Enter the amount : "))
due = input("Enter the Date : ")

display_invoice(username, amount, due)


# Sum the Values

def add(a, b):
     return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

a = int(input("Value of a : "))
b = int(input("Value of b : "))
n = input("Enter the operation : ")


if n == "+":
    print(add(a, b))
elif n == "-":
    print(sub(a, b))
elif n == "*":
    print(mul(a, b))
elif n == "/":
    print(div(a, b))
else:
    print("Invalid Statement")

# input username 
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

first = input("Enter the First name : ")
last = input("Enter the Last name : ")

fullname = create_name(first, last)

print(f"Welcome Mr. {fullname}")
