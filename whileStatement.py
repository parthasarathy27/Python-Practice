# while loop = execute some code WHILE some condition remains true

name = input("Enter your name : ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name : ")
print(f"Hello {name}")


age = int(input("Enter your age : "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age : "))
print(f"You are {age} years old")


food = input("Enter a food you like (q to quit) : ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit) : ")
print("Bye")


num = int(input("Enter a # between 1 - 10 : "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10 : "))
print(f"Your number is {num}")

# Example:

# Compound interest calculator

# A = p * (1 + r/n)^t
# A = Final amount
# p = initial principle balance
# r = interest rate
# t = number of time period


principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount : $"))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate : %"))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years : "))
    if time < 0:
        print("time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate/100), time)

print(f"Balance after {time} year/s : ${total:.2f}")
