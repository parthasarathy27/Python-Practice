# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TryError, ValueError)
#             1.try, 2.except, 3.finally

number = int(input("Enter a number : "))
print(1 / number)

# Enter a number : 0 (ZeroDivisionError: division by zero)
# Enter a number : Hello (ValueError: invalid literal for int() with base 10: 'Hello')

try:
    number = int(input("Enter a number : "))
    print(1 / number)
except ZeroDivisionError:
    print("You can't divide by Zero!")
except ValueError:
    print("Enter only numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Try Again!!!")
