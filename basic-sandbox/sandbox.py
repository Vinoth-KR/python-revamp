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

#if statemetns and boolean logic
age = 31
city = 'Chennai'

if age < 18 :
    print("You are not eligible to cast your vote.")
elif (age >= 18 and age < 65) and city == 'Bengaluru': # multiple conditions with and
    print("You are eligible to vote !.")
else:
    print("You are a senior citizen, special category to cast the vote.")

users = ['Jude', 'Alice', 'Bob', 'Jaden', 'Robert', 'admin']



# users.clear()

if(users):
    for user in users:
        if user == 'admin':
            print(f"Hello {user}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

#Oridnal numbers - 1st, 2nd, 3rd, 4th, etc.
nums = [(value+1) for value in range(9)]
for num in nums:
    ordinal = ''
    if num == 1:
        ordinal = 'st'
    elif num == 2:  
        ordinal = 'nd'
    elif num == 3:
        ordinal = 'rd'
    else:
        ordinal = 'th'
    
    print(f"{num}{ordinal}")

    dict = {"name": "Alice", "age": 30 }
    print(dict)

    nums_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
    print(nums_dict.get(2))
    print(nums_dict.get(4)) # get method to retrieve value for a key, with a default value if key is not found
    print(nums_dict.get(4, 'Not found')) 

# Both of the below for loops will give same output,
# when iterating over a dictionary, it iterates over the keys by default.
# which is explicity defined in the second loop with .keys() method.
for num in nums_dict:
    print(f"Key: {num}, Value: {nums_dict[num]}")

for num in nums_dict.keys():
    print(f"Key: {num}, Value: {nums_dict[num]}")

for k, v in nums_dict.items(): # iterating over key-value pairs with .items() method
    print(f"Key: {k}, Value: {v}")

for v in nums_dict.values(): # iterating over values with .values() method
    print(f"Value: {v}")


nums_dict2 = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


print(id(nums_dict))
print(id(nums_dict2))
print(nums_dict == nums_dict2)
print(nums_dict is nums_dict2)


#Dictionaries with nested dictionaries
users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'curie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# removing all instances of a particular item in the list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)