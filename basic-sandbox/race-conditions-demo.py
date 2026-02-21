import threading

# DEMO 1: Race condition with simple increment (harder to see due to GIL)
print("=" * 60)
print("DEMO 1: Simple increment (GIL masks race condition)")
print("=" * 60)

counter = 0

def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1  # This is NOT atomic — it's read, increment, write

# Run multiple times to see inconsistency
for attempt in range(3):
    counter = 0
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"Attempt {attempt + 1}: counter = {counter}")

# DEMO 2: Race condition with object attribute
print("\n" + "=" * 60)
print("DEMO 2: Race condition with object attribute")
print("=" * 60)

class Counter:
    def __init__(self):
        self.value = 0

counter_obj = Counter()

def increment_obj():
    global counter_obj
    for _ in range(100_000):
        temp = counter_obj.value  # Read
        temp += 1                  # Increment
        counter_obj.value = temp   # Write — These 3 steps aren't atomic!

for attempt in range(3):
    counter_obj.value = 0
    t1 = threading.Thread(target=increment_obj)
    t2 = threading.Thread(target=increment_obj)
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"Attempt {attempt + 1}: counter = {counter_obj.value} (expected 200000)")

# DEMO 3: With lock to ensure correctness
print("\n" + "=" * 60)
print("DEMO 3: With threading.Lock() to fix race condition")
print("=" * 60)

class SafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    
    def increment(self):
        for _ in range(100_000):
            with self.lock:
                temp = self.value
                temp += 1
                self.value = temp

counter_safe = SafeCounter()

for attempt in range(3):
    counter_safe.value = 0
    t1 = threading.Thread(target=counter_safe.increment)
    t2 = threading.Thread(target=counter_safe.increment)
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"Attempt {attempt + 1}: counter = {counter_safe.value} (expected 200000)")
