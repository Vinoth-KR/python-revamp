gpa = 3.5

data = ['data1', 'data2', 350]
print(data)

typed_data : list[str | int] = ["data1", "data2", 350]
print(typed_data)

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

# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the rate of interest: "))
# time = float(input("Enter the time in years: "))


# total = principal * pow((1 + rate / 100), time)

# print(f"The total amount is: {total:.2f}")


## slicing lists
cubes = [(value +1) ** 3 for value in range(15)]
print(cubes)


for cube in cubes[2:11]:
    print(cube)

print('#'* 10)
for cube in cubes[2:11:2]: # printing with a step of 2
    print(cube)
print('#'* 10)
# get top 5 cubes 
for cube in cubes[-5:]:
    print(cube)
print('#'* 10)
# get all cubes except the first 5
for cube in cubes[5:]:
    print(cube)
print('#'* 10)
# get top 5 cubes in descending order
for cube in cubes[-1:-6:-1]:
    print(cube)
print('#'* 10)
# the same can be achieved with reversed() function
cubes.sort(reverse=True)
for cube in cubes[:5]:
    print(cube)

# copying lists with slicing
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]
copied_list.append(6)
print(original_list)
print(copied_list)

original_list = copied_list

print(original_list)
print(copied_list)
print(id(original_list))
print(id(copied_list))
print(original_list is copied_list)

#Exercise : Slices
exercise_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Printing first 3 elements:', exercise_list[:3])
print('Printing last 3 elements:', exercise_list[-3:])
print('Printing middle 4 elements:', exercise_list[3:7])

#using slices with steps - :: using two colons to specify a step
print('Printing even numbers in order:', exercise_list[1:8:2]) # start at index 1, go up to index 7, step by 2