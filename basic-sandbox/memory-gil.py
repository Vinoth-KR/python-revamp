# Exploring memory management and memory address in Python

import sys
a = [1, 2, 3]
print(sys.getsizeof(a))  # Size of the list object in bytes
print(id(a))  # Memory address of the list object

b = a  # b references the same list object as a
print(id(b))  # Memory address of b (same as a)
b.append(4)  # Modifying the list through b
print(a)  # a reflects the change since it references the same list

c = a.copy()  # c is a shallow copy of a
print(id(c))  # Memory address of c (different from a and b)

print(f'a is b : {a is b}')  # True, same object
print(f'a == b : {a == b}')  # True, same contents
print(f'a is c : {a is c}')  # False, different objects
print(f'a == c : {a == c}')  # True, same contents


# Reference counting in Python
a = [1, 2, 3]           # refcount = 1
print(sys.getrefcount(a))  # Shows 2 (one for 'a', one for the arg passed to getrefcount)

b = a                    # refcount goes up — b is another reference to the SAME list
print(sys.getrefcount(a))  # Shows 3

del b                    # refcount goes back down
print(sys.getrefcount(a))  # Shows 2 again



#Default mutable arguments in Python

def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] — Surprise! It remembered the previous call.

#  Use None as default, create a new list inside the function
def add_item_fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_fixed("a"))  # ['a']
print(add_item_fixed("b"))  # ['b'] — Works as expected, no shared list.



#Global Interpreter Lock (GIL) in Python in action.

# CPU bound tasks doesn't benefit from threading due to GIL, but I/O bound tasks can.
# For CPU bound tasks, multiprocessing can be used to bypass GIL and utilize multiple cores.

import threading
import time

counter = 0 # Shared mutable state

def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1  # This is NOT atomic — it's read, increment, write

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()

print(counter) 