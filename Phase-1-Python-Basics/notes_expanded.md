# Phase 1 - Python Basics (Comprehensive Master Edition)

**Complete guide to Python fundamentals for DSA. Deep understanding, not surface-level memorization.**

---

## Table of Contents
1. [Formal Definitions](#formal-definitions)
2. [Mathematical Foundations](#mathematical-foundations)
3. [Variables & Data Types](#variables--data-types)
4. [Operations & Operators](#operations--operators)
5. [Control Flow](#control-flow)
6. [Loops](#loops)
7. [Functions](#functions)
8. [Lists & Collections](#lists--collections)
9. [Strings](#strings)
10. [Dictionaries & Sets](#dictionaries--sets)
11. [Complexity Analysis](#complexity-analysis)
12. [Worked Examples (50+)](#worked-examples)
13. [Practice Problems](#practice-problems)
14. [Common Mistakes](#common-mistakes)
15. [Interview Preparation](#interview-preparation)

---

# FORMAL DEFINITIONS

## What is Python?

**Definition (Formal):** Python is an interpreted, dynamically-typed, high-level programming language that emphasizes code readability and simplicity.

**Definition (Beginner):** Python is a set of instructions you give to a computer in English-like language.

**Key Components:**
```
Program = Data + Operations + Control Flow

Where:
- Data: What we store (variables, types)
- Operations: What we do (arithmetic, comparisons)
- Control Flow: How we make decisions (if/else, loops)
```

---

## Variable

**Mathematical Definition:** A variable is a named location in computer memory that stores a value from a domain (set of possible values).

**Notation:** 
```
var_name : Type = value
age : int = 16
name : str = "Harshi"
```

**Key Properties:**
- **Name:** Identifier for the variable
- **Type:** What kind of data it holds (int, str, float, bool)
- **Value:** The actual data stored
- **Address:** Memory location (internal to Python)
- **Scope:** Where the variable is accessible

**Example:**
```python
x = 5          # x is name, 5 is value, int is type
x = x + 1      # x now holds 6 (value changed)
y = x          # y also holds 6 (copy of value)
```

---

## Data Type

**Definition:** A data type is a classification that determines:
1. What values are valid
2. What operations can be performed
3. How much memory is needed

**Python's Built-in Data Types:**

| Type | Examples | Valid Values | Memory |
|------|----------|--------------|--------|
| int | 5, -10, 0 | All integers | Variable |
| float | 3.14, -2.5, 0.0 | All decimals | 8 bytes |
| str | "hello", "123" | Any text | Variable |
| bool | True, False | Only 2 values | 1 byte |
| list | [1, 2, 3] | Ordered collection | Variable |
| dict | {"key": "value"} | Key-value pairs | Variable |
| tuple | (1, 2, 3) | Immutable sequence | Variable |
| set | {1, 2, 3} | Unique elements | Variable |

---

## Statement vs Expression

**Definition - Expression:** A piece of code that **produces a value**
```python
5 + 3        # Expression: produces 8
2 * x        # Expression: produces a value
x > 5        # Expression: produces True/False
```

**Definition - Statement:** A piece of code that **performs an action**
```python
x = 5        # Statement: assigns value to x
print(x)     # Statement: outputs x
if x > 5:    # Statement: makes a decision
    ...
```

---

# MATHEMATICAL FOUNDATIONS

## Why Python Works - Number Systems

### Integers (Discrete Math)
```
Mathematical Definition: ℤ = {..., -2, -1, 0, 1, 2, ...}
(Set of all whole numbers, positive, negative, and zero)

In Python:
x = 5           # Positive integer
y = -10         # Negative integer
z = 0           # Zero (special integer)

Operations on integers:
- Addition: a + b
- Subtraction: a - b
- Multiplication: a * b
- Integer division: a // b (rounds down)
- Modulo: a % b (remainder)
- Exponentiation: a ** b
```

**Mathematical Properties:**
```
Closure: If a ∈ ℤ and b ∈ ℤ, then (a + b) ∈ ℤ
Proof: 5 + 3 = 8 ✓ (both integers, result is integer)

Commutativity: a + b = b + a
Example: 5 + 3 = 3 + 5 = 8

Associativity: (a + b) + c = a + (b + c)
Example: (2 + 3) + 4 = 2 + (3 + 4) = 9
```

### Floating Point Numbers (Real Numbers)
```
Mathematical Definition: ℝ = All real numbers (integers + decimals)
Includes: 3.14, -2.5, 0.0, √2, π

In Python:
x = 3.14        # Decimal with whole and fractional parts
y = -2.5        # Negative decimal
z = 2e-3        # Scientific notation: 0.002

Why floats exist:
- Measurements: height = 5.8 meters
- Probabilities: chance = 0.75
- Calculations: average = total / count
```

**Important:** Floating point is approximate!
```python
0.1 + 0.2 == 0.3  # False! (shows 0.30000000000000004)
# Why? Computers store decimals in binary (like fractional parts of powers of 2)
# Some decimals can't be represented exactly

# Safe comparison:
abs(0.1 + 0.2 - 0.3) < 0.0001  # True (within tolerance)
```

### Boolean (Logic)
```
Mathematical Definition: {True, False} (Binary/Boolean algebra)
Basis of all logic gates in computers

In Python:
is_student = True
is_logged_in = False

Boolean Operations (Logical):
AND: True AND True = True, True AND False = False
OR:  True OR False = True, False OR False = False
NOT: NOT True = False, NOT False = True

Truth Table:
A     | B     | A AND B | A OR B | NOT A
------|-------|---------|--------|-------
True  | True  | True    | True   | False
True  | False | False   | True   | False
False | True  | False   | True   | True
False | False | False   | False  | True
```

### Strings (Formal Language Theory)
```
Mathematical Definition: A string is a finite sequence of characters from an alphabet Σ

Notation: |S| = length of string S

Example: "hello"
- Alphabet: {h, e, l, l, o}
- Length: |"hello"| = 5
- Σ (Sigma) = {a,b,c,...,z,0,1,2,...,!,@,...} (all possible characters)

String Operations (Formal):
Concatenation: s1 + s2 (combining strings)
"hello" + " " + "world" = "hello world"

Repetition: s * n (repeat string n times)
"ha" * 3 = "hahaha"

Indexing: s[i] (character at position i)
"hello"[0] = 'h', "hello"[4] = 'o'

Substring: s[i:j] (characters from i to j-1)
"hello"[1:4] = "ell"
```

---

# VARIABLES & DATA TYPES

## Deep Dive: What Happens When You Create a Variable

```python
# When you write:
x = 5

# Here's what Python does internally:
# 1. Creates an integer object: object(value=5, type=int, id=140734...)
# 2. Creates a label "x" pointing to that object
# 3. Stores the reference in memory

# Visualization:
#     x ──→ [Integer Object]
#           ├─ value: 5
#           ├─ type: <class 'int'>
#           ├─ id: 140734... (memory address)
#           └─ refcount: 1

# When you do:
x = 10
# 1. Creates NEW integer object with value 10
# 2. Label "x" now points to new object
# 3. Old object (value=5) is garbage collected

# When you do:
y = x
# 1. Does NOT create new object
# 2. Label "y" points to SAME object as x
# 3. Both x and y reference same object (value=10)
```

**Key Insight - Mutable vs Immutable:**

```python
# IMMUTABLE (can't change, must create new)
x = 5
x = x + 1  # Creates NEW integer, x points to it

name = "Harshi"
name = name + " Sharma"  # Creates NEW string

# MUTABLE (can change internally)
lst = [1, 2, 3]
lst[0] = 10  # CHANGES existing list, doesn't create new one

# This matters for DSA!
def change_list(lst):
    lst[0] = 999  # Modifies original list
    
def change_int(x):
    x = x + 1  # Creates new int, doesn't change original

original_list = [1, 2, 3]
change_list(original_list)
print(original_list)  # [999, 2, 3] - CHANGED!

original_int = 5
change_int(original_int)
print(original_int)  # 5 - UNCHANGED!
```

---

## Type Conversion (Casting)

```python
# Why convert types?
# - Input from user comes as string
# - API returns numbers as strings
# - We need to change format for calculations

# Explicit conversion:
age_str = "16"
age_int = int(age_str)  # Converts "16" to 16
print(age_int + 5)  # 21 (numeric addition)

# String to float:
height_str = "5.8"
height_float = float(height_str)
print(height_float * 100)  # 580 (numeric)

# Integer to string:
count = 42
count_str = str(count)
print("You have " + count_str + " problems")  # String concatenation

# Float to integer (truncates decimal):
pi = 3.14159
pi_int = int(pi)  # 3 (NOT rounded, truncated)

# Boolean conversion (truthy/falsy):
bool(0)      # False (0 is "falsy")
bool(1)      # True (any non-zero is "truthy")
bool("")     # False (empty string is falsy)
bool("hello")# True (non-empty string is truthy)
bool([])     # False (empty list is falsy)
bool([1,2])  # True (non-empty list is truthy)
```

---

# OPERATIONS & OPERATORS

## Arithmetic Operators (Mathematical Operations)

```python
a = 10
b = 3

# Addition
print(a + b)  # 13
# Mathematical: a + b where + is binary operator

# Subtraction
print(a - b)  # 7

# Multiplication
print(a * b)  # 30

# Division (Float division - result is always float)
print(a / b)  # 3.3333...
# Mathematical: a ÷ b

# Integer Division (Floor division - rounds DOWN)
print(a // b)  # 3
# Why: 10 ÷ 3 = 3.333..., floor is 3
# Note: floor(-10 // 3) = -4 (not -3, rounds toward negative infinity)

# Modulo (Remainder after division)
print(a % b)  # 1
# Why: 10 = 3*3 + 1, so remainder is 1
# Mathematical: a mod b = a - b * floor(a/b)

# Exponentiation
print(a ** b)  # 1000
# Mathematical: a^b = 10^3

# Operator precedence (PEMDAS):
# ** (exponentiation) > *, /, //, % > +, -
result = 2 + 3 * 4 ** 2
# Step 1: 4 ** 2 = 16
# Step 2: 3 * 16 = 48
# Step 3: 2 + 48 = 50
```

## Comparison Operators (Boolean Results)

```python
a = 5
b = 10

# Equal to
print(a == b)  # False

# Not equal to
print(a != b)  # True

# Greater than
print(a > b)   # False

# Less than
print(a < b)   # True

# Greater than or equal
print(a >= b)  # False

# Less than or equal
print(a <= b)  # True

# Chained comparisons (special to Python):
x = 5
print(0 < x < 10)  # True (equivalent to x > 0 AND x < 10)
print(0 < x < 3)   # False

# Important for DSA: Use == correctly
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True (same contents)
print(list1 is list2)  # False (different objects)
```

## Logical Operators (Boolean Logic)

```python
# AND (both must be true)
print(True and True)   # True
print(True and False)  # False
print(False and False) # False

age = 16
is_student = True
can_drive = (age >= 16) and is_student  # Both conditions must be true

# OR (at least one must be true)
print(True or False)   # True
print(False or False)  # False

has_passport = False
has_driving_license = True
can_travel = has_passport or has_driving_license  # At least one true

# NOT (inverts boolean)
print(not True)   # False
print(not False)  # True

is_logged_in = False
is_admin = not is_logged_in  # True

# Short-circuit evaluation (important for efficiency)
# AND: if first is False, doesn't evaluate second
def expensive_check():
    print("Running expensive check...")
    return True

if False and expensive_check():  # expensive_check() NEVER runs
    print("Done")
# Output: Nothing (expensive_check not called!)

# OR: if first is True, doesn't evaluate second
if True or expensive_check():  # expensive_check() NEVER runs
    print("Done")
# Output: Done (expensive_check not called!)
```

---

# CONTROL FLOW

## If Statements (Making Decisions)

```python
# Basic if:
age = 16
if age >= 18:
    print("You are an adult")

# If with else:
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# If with elif (else if):
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"Grade: {grade}")  # Grade: C

# Nested if:
age = 16
is_student = True
if age >= 16:
    if is_student:
        print("You are a young student")
    else:
        print("You are 16 but not a student")

# Ternary operator (one-liner if-else):
status = "adult" if age >= 18 else "minor"
# Equivalent to: if age >= 18: status = "adult" else: status = "minor"

# Common pattern for DSA:
def max_of_two(a, b):
    return a if a > b else b
print(max_of_two(5, 10))  # 10
```

---

# LOOPS

## For Loop (Iterating a Known Number of Times)

```python
# Basic for loop - repeat 5 times
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# range(n) generates: 0, 1, 2, ..., n-1
# range(start, end) generates: start, start+1, ..., end-1
for i in range(2, 5):
    print(i)  # Prints 2, 3, 4

# range(start, end, step) with custom step
for i in range(0, 10, 2):
    print(i)  # Prints 0, 2, 4, 6, 8

for i in range(10, 0, -1):
    print(i)  # Prints 10, 9, 8, ..., 1 (counting down)

# For loop with list (most common in DSA):
numbers = [10, 20, 30, 40]
for num in numbers:
    print(num * 2)  # Prints 20, 40, 60, 80

# For loop with string:
word = "hello"
for char in word:
    print(char)  # Prints h, e, l, l, o

# Enumerate (get both index and value):
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # Prints: 0: apple, 1: banana, 2: orange

# Common DSA pattern - iterating with index:
# DON'T do this:
for i in range(len(fruits)):
    print(fruits[i])

# DO this instead:
for i, fruit in enumerate(fruits):
    print(fruit)
```

## While Loop (Repeat Until Condition is False)

```python
# Basic while loop:
count = 0
while count < 5:
    print(count)
    count = count + 1
# Prints: 0, 1, 2, 3, 4

# While with break (exit early):
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break  # Exit loop immediately
    print(f"You entered: {user_input}")

# While with continue (skip to next iteration):
count = 0
while count < 5:
    count = count + 1
    if count == 3:
        continue  # Skip printing 3
    print(count)
# Prints: 1, 2, 4, 5

# Common DSA pattern - binary search uses while:
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

## Loop Patterns (Critical for DSA)

```python
# Pattern 1: Iterate and accumulate
total = 0
for num in [1, 2, 3, 4, 5]:
    total = total + num
print(total)  # 15

# Pattern 2: Count occurrences
count = 0
for num in [1, 2, 2, 3, 2, 4]:
    if num == 2:
        count = count + 1
print(count)  # 3

# Pattern 3: Find first matching element
for num in [1, 2, 3, 4, 5]:
    if num > 3:
        print(num)  # 4 (stops after first match)
        break

# Pattern 4: Transform elements (create new list)
squares = []
for num in [1, 2, 3, 4, 5]:
    squares.append(num ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Pattern 5: Nested loops (two pointers)
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
# Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)
```

---

# FUNCTIONS

## Formal Definition

**Mathematical Definition:** A function f: X → Y is a relation that maps each element x ∈ X to exactly one element y ∈ Y.

**Programming Definition:** A function is a reusable block of code that takes input (parameters), performs operations, and optionally returns output.

```python
# Function syntax:
def function_name(parameter1, parameter2):
    """Docstring explaining what function does"""
    # Function body
    result = parameter1 + parameter2
    return result

# Function call:
output = function_name(5, 10)  # output = 15
```

## Function Components

```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of integers or floats
    
    Returns:
        float: The average of the numbers
    
    Time Complexity: O(n) where n is length of list
    Space Complexity: O(1)
    """
    if len(numbers) == 0:  # Edge case
        return 0
    
    total = sum(numbers)  # sum() loops through all elements
    average = total / len(numbers)  # division
    return average

# Usage:
result = calculate_average([10, 20, 30])
print(result)  # 20.0

# Function components:
# 1. def: keyword to define function
# 2. calculate_average: function name (snake_case)
# 3. (numbers): parameter (what function takes)
# 4. Docstring: explains function purpose
# 5. Body: operations inside {}
# 6. return: sends result back to caller
```

## Parameters vs Arguments

```python
# PARAMETERS: variables in function definition
def greet(name):  # "name" is PARAMETER
    print(f"Hello, {name}!")

# ARGUMENTS: actual values passed when calling function
greet("Harshi")  # "Harshi" is ARGUMENT

# Positional arguments:
def add(a, b):
    return a + b

result = add(5, 3)  # 5 is first arg, 3 is second

# Keyword arguments:
result = add(b=3, a=5)  # Order doesn't matter

# Default parameters:
def greet(name="Friend"):
    return f"Hello, {name}!"

print(greet())      # "Hello, Friend!"
print(greet("Bob")) # "Hello, Bob!"

# Variable number of arguments (*args):
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15

# Keyword arguments as dictionary (**kwargs):
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Harshi", age=16, city="India")
# name: Harshi
# age: 16
# city: India
```

## Return Values and None

```python
# Function returns a value:
def square(x):
    return x ** 2

result = square(5)
print(result)  # 25

# Function with multiple return values (returns tuple):
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([3, 1, 4, 1, 5])
print(minimum, maximum)  # 1 5

# Function that doesn't return (returns None):
def print_hello():
    print("Hello!")
    # No return statement

result = print_hello()
print(result)  # None

# Early return (exit function early):
def check_age(age):
    if age < 0:
        return "Invalid age"
    if age < 13:
        return "Child"
    if age < 18:
        return "Teenager"
    return "Adult"

print(check_age(16))  # "Teenager"
```

## Scope - Where Variables are Accessible

```python
# Global scope: accessible everywhere
global_var = "I'm global"

def my_function():
    # Local scope: accessible only in this function
    local_var = "I'm local"
    print(global_var)   # ✓ Can access global
    print(local_var)    # ✓ Can access local

my_function()
# print(local_var)  # ✗ ERROR! local_var not accessible outside function

# Variable shadowing (local variable hides global):
x = 10  # Global x

def shadow():
    x = 20  # Local x (shadows global x)
    print(x)  # 20 (uses local x)

shadow()
print(x)  # 10 (global x unchanged)

# Using global keyword (modifying global from function):
counter = 0

def increment():
    global counter  # Tell Python to use global counter
    counter = counter + 1

increment()
print(counter)  # 1
```

---

# LISTS & COLLECTIONS

## Lists - Ordered, Mutable Collections

```python
# Creating lists:
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [1, [2, 3], [4, [5, 6]]]

# Accessing elements (0-indexed):
numbers = [10, 20, 30, 40, 50]
print(numbers[0])   # 10 (first element)
print(numbers[-1])  # 50 (last element)
print(numbers[-2])  # 40 (second from last)

# Slicing (getting sublist):
print(numbers[1:4])    # [20, 30, 40] (index 1,2,3)
print(numbers[:3])     # [10, 20, 30] (first 3)
print(numbers[2:])     # [30, 40, 50] (from index 2 onward)
print(numbers[::2])    # [10, 30, 50] (every 2nd element)
print(numbers[::-1])   # [50, 40, 30, 20, 10] (reversed)

# List operations:
lst = [1, 2, 3]
lst.append(4)               # Add to end: [1,2,3,4]
lst.insert(0, 0)            # Add at position: [0,1,2,3,4]
lst.extend([5, 6])          # Add multiple: [0,1,2,3,4,5,6]
lst.remove(3)               # Remove value 3: [0,1,2,4,5,6]
popped = lst.pop()          # Remove last, return it: 6
value = lst.pop(1)          # Remove at index 1, return it: 1

# List comprehension (create list with pattern):
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Important: Lists are mutable (changeable)
lst = [1, 2, 3]
lst[0] = 10
print(lst)  # [10, 2, 3] - CHANGED
```

## Tuples - Ordered, Immutable Collections

```python
# Creating tuples:
empty_tuple = ()
single_tuple = (1,)  # Comma required for single element!
pair = (1, 2)
triple = (1, 2, 3)

# Accessing (same as lists):
print(pair[0])  # 1
print(pair[-1]) # 2

# Important: Tuples are IMMUTABLE (can't change)
# pair[0] = 10  # ERROR! Can't modify tuple

# Why tuples?
# 1. Faster than lists (immutable = can optimize)
# 2. Can be used as dictionary keys (lists can't)
# 3. Prevent accidental modification

# Unpacking:
a, b = (1, 2)
print(a)  # 1
print(b)  # 2

# Multiple return values (returns tuple):
def get_info():
    return ("Harshi", 16, "India")

name, age, city = get_info()
```

---

# STRINGS

## String Operations and Methods

```python
# String creation:
s1 = "hello"
s2 = 'world'
s3 = """Multi-line
string"""

# String indexing (0-based):
s = "hello"
print(s[0])   # 'h'
print(s[-1])  # 'o'

# String slicing:
print(s[1:4])    # 'ell'
print(s[::-1])   # 'olleh' (reversed)

# String methods:
s = "Hello World"
print(s.lower())            # 'hello world'
print(s.upper())            # 'HELLO WORLD'
print(s.startswith("Hello"))# True
print(s.endswith("World"))  # True
print(s.find("World"))      # 6 (index of first occurrence)
print(s.replace("World", "Python"))  # 'Hello Python'
print(s.split(" "))         # ['Hello', 'World'] (split into list)

# String formatting:
name = "Harshi"
age = 16

# f-strings (modern Python):
print(f"My name is {name} and I am {age} years old")

# .format():
print("My name is {} and I am {}".format(name, age))

# Concatenation:
greeting = "Hello" + " " + "World"
print(greeting)  # "Hello World"

# Important: Strings are IMMUTABLE
s = "hello"
# s[0] = 'H'  # ERROR! Can't modify string

# String length:
print(len("hello"))  # 5
```

---

# DICTIONARIES & SETS

## Dictionaries - Key-Value Pairs

```python
# Creating dictionaries:
empty_dict = {}
person = {"name": "Harshi", "age": 16, "city": "India"}
mixed_keys = {1: "one", "two": 2, 3.0: [1, 2, 3]}

# Accessing values:
print(person["name"])  # "Harshi"
print(person.get("age"))  # 16
print(person.get("country", "Unknown"))  # "Unknown" (default if missing)

# Adding/modifying:
person["age"] = 17  # Modify
person["country"] = "India"  # Add new key

# Dictionary iteration:
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary methods:
print(person.keys())    # dict_keys(['name', 'age', ...])
print(person.values())  # dict_values(['Harshi', 17, ...])
print("name" in person) # True (check if key exists)
person.pop("country")   # Remove key
```

## Sets - Unique, Unordered Collections

```python
# Creating sets:
empty_set = set()  # {} is dictionary!
numbers = {1, 2, 3, 4, 5}
unique = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3} (duplicates removed)

# Set operations:
s1 = {1, 2, 3}
s2 = {2, 3, 4}

print(s1 | s2)      # {1, 2, 3, 4} (union - all elements)
print(s1 & s2)      # {2, 3} (intersection - common elements)
print(s1 - s2)      # {1} (difference - in s1 but not s2)
print(s1 ^ s2)      # {1, 4} (symmetric difference)

# Set methods:
s = {1, 2, 3}
s.add(4)            # {1, 2, 3, 4}
s.remove(2)         # {1, 3, 4} (error if not found)
s.discard(5)        # {1, 3, 4} (no error if not found)

# Common use: Remove duplicates
lst = [1, 2, 2, 3, 3, 3]
unique_lst = list(set(lst))  # [1, 2, 3]
```

---

# COMPLEXITY ANALYSIS

## Time Complexity of Python Operations

```python
# O(1) - Constant time
lst = [1, 2, 3, 4, 5]
value = lst[0]           # Direct access by index
lst.append(6)            # Average case
d = {"key": "value"}
d["key"] = "new_value"   # Dictionary lookup

# O(n) - Linear time
total = sum(lst)         # Loop through all n elements
max_val = max(lst)       # Check all elements
for num in lst:          # Explicit loop
    print(num)

# O(n log n) - Linearithmic time
sorted_lst = sorted(lst) # Sorting algorithm

# O(n²) - Quadratic time
for i in range(len(lst)):
    for j in range(len(lst)):
        print(lst[i], lst[j])  # Nested loop

# O(2^n) - Exponential (avoid!)
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)  # Exponential branching
```

## Space Complexity

```python
# O(1) - Constant space
def sum_first_five(lst):
    return lst[0] + lst[1] + lst[2] + lst[3] + lst[4]
# Only uses variables: no extra space

# O(n) - Linear space
def create_doubled(lst):
    result = []
    for num in lst:
        result.append(num * 2)
    return result  # Stores n elements

# O(n²) - Quadratic space
def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * j)
        matrix.append(row)
    return matrix  # Stores n² elements
```

---

# WORKED EXAMPLES

## Example 1: Find Maximum Element

```python
# Problem: Find the largest number in a list
# Input: [3, 1, 4, 1, 5, 9, 2, 6]
# Output: 9

# Approach 1: Using built-in max()
def find_max_builtin(numbers):
    return max(numbers)

# Approach 2: Manual iteration
def find_max_manual(numbers):
    if len(numbers) == 0:
        return None
    
    max_val = numbers[0]  # Start with first element
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

# Approach 3: Using while loop
def find_max_while(numbers):
    if len(numbers) == 0:
        return None
    
    max_val = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > max_val:
            max_val = numbers[i]
        i += 1
    return max_val

# Time Complexity: O(n) for all approaches (loop through n elements)
# Space Complexity: O(1) (only one variable max_val)

# Test:
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(find_max_manual(numbers))  # 9
```

## Example 2: Check If Number is Prime

```python
# Problem: Determine if number is prime
# Input: 17
# Output: True (only divisible by 1 and itself)

def is_prime(n):
    """
    Check if n is prime.
    
    Time Complexity: O(√n) - loop up to sqrt(n)
    Space Complexity: O(1)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to √n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

# Mathematical insight:
# If n has divisor > √n, it must also have divisor < √n
# So we only need to check up to √n

# Example: is_prime(17)
# √17 ≈ 4.1
# Check: 17 % 2 = 1 ✓, 17 % 3 = 2 ✓
# Result: True

print(is_prime(17))   # True
print(is_prime(18))   # False
print(is_prime(2))    # True
print(is_prime(1))    # False
```

## Example 3: Reverse a List

```python
# Problem: Reverse a list
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# Approach 1: Built-in
def reverse_builtin(lst):
    return lst[::-1]

# Approach 2: Using reversed() function
def reverse_function(lst):
    return list(reversed(lst))

# Approach 3: Manual with new list
def reverse_new_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):  # Start from end
        result.append(lst[i])
    return result

# Approach 4: In-place reversal (two pointers)
def reverse_inplace(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        # Swap elements
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

# Complexity:
# Approach 1,2: Time O(n), Space O(n)
# Approach 3: Time O(n), Space O(n)
# Approach 4: Time O(n), Space O(1) ← Best!

numbers = [1, 2, 3, 4, 5]
print(reverse_inplace(numbers.copy()))  # [5, 4, 3, 2, 1]
```

---

# PRACTICE PROBLEMS

## Easy Problems (Understand Basics)

### Problem 1: Sum of Numbers
```python
# Given a list of numbers, return their sum
# Example: [1, 2, 3, 4] → 10

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4]))  # 10
```

### Problem 2: Count Occurrences
```python
# Count how many times an element appears
# Example: [1, 2, 2, 3, 2] → count(2) = 3

def count_element(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

print(count_element([1, 2, 2, 3, 2], 2))  # 3
```

### Problem 3: Find First Even Number
```python
# Return first even number in list
# Example: [1, 3, 5, 2, 4] → 2

def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

print(find_first_even([1, 3, 5, 2, 4]))  # 2
```

---

## Medium Problems (Practice Combinations)

### Problem 4: Two Sum
```python
# Find two numbers that add up to target
# Example: [2, 7, 11, 15], target=9 → [0, 1] (indices of 2 and 7)

def two_sum_bruteforce(numbers, target):
    """Brute force: O(n²) time, O(1) space"""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None

def two_sum_optimal(numbers, target):
    """Hash map: O(n) time, O(n) space"""
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

print(two_sum_bruteforce([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum_optimal([2, 7, 11, 15], 9))     # [0, 1]
```

---

# COMMON MISTAKES

## ❌ Mistake 1: Off-by-One Error in Loops

```python
# WRONG:
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers) + 1):  # Goes 0 to 5, but max index is 4!
    print(numbers[i])  # ERROR on last iteration!

# RIGHT:
for i in range(len(numbers)):  # Goes 0 to 4
    print(numbers[i])  # ✓ Works

# Or even better:
for num in numbers:  # Don't use index if you don't need it
    print(num)
```

## ❌ Mistake 2: Mutable Default Arguments

```python
# WRONG:
def add_to_list(item, lst=[]):
    lst.append(item)
    return lst

result1 = add_to_list(1)  # [1]
result2 = add_to_list(2)  # [1, 2] - SAME list!
print(result1 is result2) # True (same object!)

# RIGHT:
def add_to_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

result1 = add_to_list(1)  # [1]
result2 = add_to_list(2)  # [2] - Different list
```

## ❌ Mistake 3: Modifying List While Iterating

```python
# WRONG:
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Modifies during iteration!
print(numbers)  # [1, 3, 5] - Skipped some elements!

# RIGHT:
numbers = [1, 2, 3, 4, 5]
# Option 1: Create new list
evens = [num for num in numbers if num % 2 == 0]

# Option 2: Iterate over copy
for num in numbers.copy():
    if num % 2 == 0:
        numbers.remove(num)
```

---

# INTERVIEW PREPARATION

## Key Concepts to Master

1. **Variables & Data Types** - Know the difference, when to use each
2. **Loops** - For/while, break/continue, nested loops
3. **Functions** - Parameters, return values, scope
4. **Lists** - Indexing, slicing, common methods
5. **Dictionaries** - Key lookup, iteration
6. **Time Complexity** - Understand O(1), O(n), O(n²)

## Interview Questions

**Q1: Explain mutable vs immutable with examples**
```
A: Mutable objects can be changed in-place:
   - Lists: lst[0] = 10 changes the list
   - Dictionaries: d["key"] = "new" changes the dict
   
   Immutable objects must be reassigned:
   - Strings: s = s + "!" creates new string
   - Integers: x = x + 1 creates new integer
   - Tuples: Can't modify at all
   
   This matters for functions - modifying mutable arguments
   changes the original, but modifying immutable doesn't.
```

**Q2: What's time complexity of list.append()?**
```
A: Amortized O(1) - most of the time instant, but sometimes
   needs to resize which takes O(n). Over many operations,
   averages to O(1).
```

**Q3: Difference between list and tuple?**
```
A: 
| Property | List | Tuple |
|----------|------|-------|
| Mutable | Yes | No |
| Speed | Slower | Faster |
| Methods | Many | Few |
| Dict key | No | Yes |
| Use case | Dynamic data | Fixed data |
```

---

**Master these fundamentals. This is the foundation for all DSA!** 🎯

