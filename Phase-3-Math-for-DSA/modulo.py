"""
TOPIC: Modulo Operations
Difficulty: Beginner

Modulo (%) gives the REMAINDER after division.
Why: Common in hashing, circular arrays, and many algorithms.
"""

print("=== MODULO OPERATIONS ===\n")

# Basic modulo
# Why: Get remainder of division
print("Basic Modulo:")
print(f"17 % 5 = {17 % 5}")    # 17 = 3*5 + 2, remainder = 2
print(f"20 % 3 = {20 % 3}")    # 20 = 6*3 + 2, remainder = 2
print(f"10 % 4 = {10 % 4}")    # 10 = 2*4 + 2, remainder = 2
print(f"15 % 5 = {15 % 5}")    # 15 = 3*5 + 0, remainder = 0

# Check if number is even or odd
# Why: Even numbers have remainder 0 when divided by 2
print("\nEven/Odd Check:")
for num in [10, 15, 20, 23]:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Circular array indexing
# Why: When you go past the end, wrap to the beginning
# Example: Round-robin scheduling
print("\nCircular Indexing:")
position = 25
array_size = 10
circular_pos = position % array_size
print(f"Position {position} in array of size {array_size} → index {circular_pos}")

# Another example: Clock arithmetic
print("\nClock Arithmetic:")
current_hour = 15  # 3 PM
add_hours = 11
new_hour = (current_hour + add_hours) % 24
print(f"3 PM + 11 hours = hour {new_hour} (next day)")

# Repeat pattern every n numbers
# Why: Some algorithms process in batches
print("\nRepeat Pattern:")
for i in range(10):
    group = i % 3  # Group 0, 1, 2, repeat
    print(f"Number {i} belongs to group {group}", end=" | ")
    if (i + 1) % 3 == 0:
        print()

# Isolate last digit
# Why: Common operation
print("\nIsolate Last Digit:")
numbers = [123, 456, 789]
for num in numbers:
    last_digit = num % 10
    print(f"Last digit of {num}: {last_digit}")

# Isolate last n digits
# Why: Extract parts of a number
print("\nIsolate Last N Digits:")
num = 123456
last_2 = num % 100      # 56
last_3 = num % 1000     # 456
print(f"Last 2 digits of {num}: {last_2}")
print(f"Last 3 digits of {num}: {last_3}")

# Modulo with negative numbers (Python behavior)
# Why: Important to know
print("\nModulo with Negatives:")
print(f"-10 % 3 = {-10 % 3}")   # Python: 2
print(f"10 % -3 = {10 % -3}")   # Python: -2
# Note: Python's modulo always returns result with sign of divisor
