#EAFP - Easier to ask for forgiveness than permission - Pythonic code.

# Try getting some numbers from the user and divide them. ]
# If the user enters something that isn't a number, or if they try to divide by zero, catch the exception and print an error message.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result:.2f}")   
except (TypeError, ValueError):
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

