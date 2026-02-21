gpa = 3.5


#Type casting
#converting values from float to integer
gpa = int(gpa)
print(gpa)
print(type(gpa))

#exploring inputs and type casting with explicit and implicit
# item = input("Item to buy? ")
# price = float(input("Price of the item? "))
# quantity = int(input("How many quantity? "))

# total = price * quantity
# print(f"You have bought {quantity} x {item}/s")
# print(f"Total cost is {total}")

#finding the circumference of the circle using math module

# import math

# radius = float(input('Enter the radius of the circle? '))

# circumference = 2 * math.pi * radius

# print(f"The circumference of the circle is : {round(circumference, 4)}")

#String indexes and slices

testText = "Racecar"

print(testText.lower() == testText.lower()[::-1])


#Compound Interest calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))


total = principal * pow((1 + rate / 100), time)

print(f"The total amount is: {total:.2f}")
