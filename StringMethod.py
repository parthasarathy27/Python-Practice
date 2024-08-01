'''
#name = input("Enter your full name : ")

phone_number = input("Enter Your Phone Number : ")

#result = name.find("G")
#result = name.rfind("h")
#result = name.capitalize()
#result = name.upper()
#result = name.lower()
#result = name.isdigit()
#result = name.isalpha()

#result = phone_number.count("-")
result = phone_number.replace("-", " ")

print(result)
print(help(str))
'''

# validate user input exercise
# 1. username is no more than 12 charaters
# 2. username must not contain spaces
# 3. username must not contain digits

#Example code

username = input("Enter the username : ")

if len(username) > 12:
    print("your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("your username can't contain spaces")
elif not username.isalpha():
    print("your username can't contain numbers")
else:
    print(f"Welcome {username}")
