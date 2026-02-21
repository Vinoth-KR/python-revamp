#EAFP - Easier to ask for forgiveness than permission - Pythonic code.

# Try getting some numbers from the user and divide them. ]
# If the user enters something that isn't a number, or if they try to divide by zero, catch the exception and print an error message.
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     result = num1 / num2
#     print(f"The result of {num1} divided by {num2} is: {result:.2f}")   
# except (TypeError, ValueError):
#     print("Error: Please enter valid numbers.")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")


#Type hinting 

def greet (name : str, times: int = 1) -> str:
    try:
        name = process_str_value(name)
        times = process_int_value(times)
        return(f"Hello, {name}! " * times).strip()
    except ValueError as e:
        raise e
    
        

def process_str_value(value : str | int) -> str:
    return str(value)

def process_int_value(value : int | str) -> int:
    try:
        if not isinstance(value, int):
            value = int(value)
        if value < 1:
            value = 1

        return value
    except ValueError:
        raise ValueError("Value must be an integer or a string that can be converted to an integer.")


def greet2(name : str, times : int = 1) -> str:
    """Greet a person a specified number of times."""
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    if not isinstance(times, int) or times < 1:
        raise ValueError("Times must be a positive integer.")
    
    return " ".join([f"Hello, {name}!" for _ in range(times)])


print(greet(123, "3"))
#print(greet2(123, "3"))


#Typed Dicts

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    email: str

def create_user(name: str, age: int, email: str) -> User:
    return {"name": name, "age": age, "email": email}

def display_user_info(user: User) -> None:
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"Email: {user['email']}")

user1 = create_user("Alice", 30, "alice@test.com")
user2 = create_user("Bob", 25, "bob@test.com")

display_user_info(user1)
display_user_info(user2)

#Callables - Functions in C#, for example - Func<int, int, int> - a function that takes two integers and returns an integer.

#Exercise: Create a function that takes a list of numbers and a Callable that defines an operation to perform on those numbers (e.g., sum, product, average). 
# The function should return the result of applying the operation to the list of numbers.

from typing import Callable

def apply_operation(a: int, b: int, operation: Callable[[int, int], float]) -> float:
    return operation(a, b)

def add(x: int, y: int) -> float:
    return x + y

def multiply(x: int, y: int) -> float:
    return x * y

def divide(x: int, y: int) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

addresult = apply_operation(5, 3, add)
multiplyresult = apply_operation(5, 3, multiply)
dividresult = apply_operation(10, 2, divide)
print(f"Addition result: {addresult:.2f}")
print(f"Multiplication result: {multiplyresult:.2f}")
print(f"Division result: {dividresult:.2f}")

#Exercise : Write a function merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int] 
# that merges two dictionaries, summing values for duplicate keys. Annotate everything.

def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    merged : dict[str, int] ={}
    for key in (set(d1.keys()).union(d2.keys())):
        merged[key] = d1.get(key, 0) + d2.get(key, 0)

    return merged

#Example usage:
dict1: dict[str, int] = {"a": 1, "b": 2, "c": 3}
dict2: dict[str, int] = {"b": 3, "c": 4, "d": 5}
merged_dict: dict[str, int] = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
