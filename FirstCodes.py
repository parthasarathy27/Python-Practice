# 1 Mad libs games

adjective1 = input("Enter an adjective1 : ")
noun = input("Enter a noun : ")
adjective2 = input("Enter an adjective2 : ")
verb = input("Enter a verb : ")
adjective3 = input("Enter an adjective3 : ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw {noun}")
print(f"{noun} was {adjective2} and {verb}")
print(f"I was {adjective3}")

# 2 area calc

length = float(input("Enter the length of a rectangle : "))
width = float(input("Enter the width of a rectangle : "))
height = float(input("Enter the height of a rectangle : "))

area = length * width
volume = length * width * height

print(f"The area is : {area} cm^2")
print(f"The Volume is : {volume} cm^3")

# 3 shopping card

item = input("What item would you like to buy? : ")
price = float(input("what is the price? : "))
quantity = int(input("How many would you like? : "))

total = price * quantity

print(f"You have bought {quantity} x {item}'s")
print(f"Your total amount is : Rs.{round(total, 2)}")
