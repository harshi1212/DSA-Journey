"""
TOPIC: Functions - The Most Important Concept
Difficulty: Beginner

Functions are reusable blocks of code.
Why: Write once, use many times. Don't copy-paste!
"""

# ── PART 1: Basic Function ────────────────────────────
# A function is code you organize and reuse

print("=== BASIC FUNCTIONS ===\n")

# Define a function (create it)
# Why: Create a block of code that does one job
def say_hello():
    # This is the function body (indented code)
    print("Hello! Welcome to DSA!")

# Call/invoke the function (use it)
# Why: Run the code whenever you need it
say_hello()  # Runs the function
say_hello()  # Run it again
say_hello()  # Run it again (no copy-paste!)

# ── PART 2: Functions with Parameters (Inputs) ────────────────────────────
# Why: Same function, different data

print("\n=== FUNCTIONS WITH PARAMETERS ===\n")

# Function with 1 parameter
# Why: Function can work with different values
def greet_person(name):
    # "name" is a parameter (placeholder for input)
    print(f"Hello, {name}! Nice to meet you.")

# Call with different values (arguments)
# Why: Pass actual data when calling
greet_person("Harshi")  # Pass "Harshi"
greet_person("Alice")   # Pass "Alice"
greet_person("Bob")     # Pass "Bob"

# Function with multiple parameters
# Why: Function can take multiple inputs
def add_numbers(a, b):
    # a and b are parameters
    result = a + b
    return result  # Send answer back to caller

# Call with arguments
sum1 = add_numbers(10, 20)  # 10 and 20 are arguments
print(f"\n10 + 20 = {sum1}")

sum2 = add_numbers(5, 7)
print(f"5 + 7 = {sum2}")

# ── PART 3: Return Statement ────────────────────────────
# return: Send value back to the caller
# Why: The function computes something, you need the result

print("\n=== RETURN STATEMENT ===\n")

def multiply(a, b):
    # Calculate inside function
    result = a * b
    # Return the answer back
    return result

# Get the returned value
answer = multiply(6, 7)
print(f"6 × 7 = {answer}")

# Return without storing
print(f"3 × 4 = {multiply(3, 4)}")

# Function that checks something
# Why: Make decision-making reusable
def is_even(number):
    # Check if even
    if number % 2 == 0:
        return True  # Yes, it's even
    else:
        return False  # No, it's odd

print(f"\nIs 10 even? {is_even(10)}")  # True
print(f"Is 7 even? {is_even(7)}")   # False

# ── PART 4: Default Parameters ────────────────────────────
# Why: Function works without arguments if not provided

print("\n=== DEFAULT PARAMETERS ===\n")

def power(base, exponent=2):
    # exponent has a default value of 2
    # If you don't provide it, it uses 2
    result = base ** exponent
    return result

print(f"5^2 = {power(5)}")  # Uses default exponent=2
print(f"5^3 = {power(5, 3)}")  # Provides custom exponent=3
print(f"2^10 = {power(2, 10)}")  # Provides custom exponent=10

# ── PART 5: Multiple Return Values ────────────────────────────
# Why: Sometimes function needs to return multiple values

print("\n=== MULTIPLE RETURNS ===\n")

def divide_with_remainder(a, b):
    # Calculate quotient and remainder
    quotient = a // b
    remainder = a % b
    return quotient, remainder  # Return both as tuple

# Unpack the returned values
q, r = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")

# ── PART 6: Variable Scope ────────────────────────────
# Why: Variables inside function don't affect outside

print("\n=== VARIABLE SCOPE ===\n")

global_var = "I'm global"  # Created outside function

def modify_variable():
    # "x" inside function is different from outside
    x = "I'm local"
    print(f"Inside function: {x}")

modify_variable()
print(f"Outside function: {global_var}")
# print(x)  # Error! x doesn't exist here

# ── PART 7: Function Patterns (Important!) ────────────────────────────
# These appear in every DSA problem

print("\n=== IMPORTANT PATTERNS ===\n")

# Pattern 1: Process a list and return result
def sum_list(numbers):
    # Take a list, return sum
    total = 0
    for num in numbers:
        total = total + num
    return total

result = sum_list([1, 2, 3, 4, 5])
print(f"Sum of [1,2,3,4,5] = {result}")

# Pattern 2: Transform a list
def double_all(numbers):
    # Take a list, return doubled list
    result = []
    for num in numbers:
        result.append(num * 2)
    return result

doubled = double_all([1, 2, 3])
print(f"Doubled [1,2,3] = {doubled}")

# Pattern 3: Filter a list (keep only matching items)
def get_evens(numbers):
    # Take a list, return only even numbers
    result = []
    for num in numbers:
        if num % 2 == 0:  # If even
            result.append(num)
    return result

evens = get_evens([1, 2, 3, 4, 5, 6])
print(f"Evens from [1-6] = {evens}")

# Pattern 4: Search in a list
def find_target(numbers, target):
    # Find position of target in list
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i  # Found! Return position
    return -1  # Not found

position = find_target([10, 20, 30, 40], 30)
print(f"Position of 30: {position}")

# ── PART 8: Good Function Practice ────────────────────────────

print("\n=== FUNCTION CHECKLIST ===\n")

def calculate_average(grades):
    """
    Calculate average of grades.
    Why: Docstring explains what function does
    """
    # Input validation
    if len(grades) == 0:
        return 0  # Handle edge case
    
    # Do the calculation
    total = sum(grades)
    average = total / len(grades)
    
    # Return result
    return average

# Test it
result = calculate_average([90, 85, 95])
print(f"Average of [90,85,95] = {result}")

result = calculate_average([])
print(f"Average of empty list = {result}")

# ── Test Your Understanding ────────────────────────────
print("\n" + "="*50)
print("QUICK QUIZ")
print("="*50)

# 1. Write function to check if number is positive
def is_positive(num):
    return num > 0

print(f"\n1. Is 5 positive? {is_positive(5)}")
print(f"   Is -3 positive? {is_positive(-3)}")

# 2. Write function to count vowels in word
def count_vowels(word):
    count = 0
    vowels = "aeiouAEIOU"
    for letter in word:
        if letter in vowels:
            count = count + 1
    return count

print(f"\n2. Vowels in 'HELLO': {count_vowels('HELLO')}")
print(f"   Vowels in 'PYTHON': {count_vowels('PYTHON')}")

# 3. Write function to get max of two numbers
def get_max(a, b):
    if a > b:
        return a
    else:
        return b

print(f"\n3. Max of 10 and 20: {get_max(10, 20)}")
print(f"   Max of 50 and 30: {get_max(50, 30)}")

print("\n✓ Complete Phase 1.3 to master functions!")
