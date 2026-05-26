"""
TOPIC: Variables and Data Types
Difficulty: Beginner

This file teaches you how to store information in Python.
A variable is a named container. Think of it like a labeled box.
"""

# ── PART 1: Creating Variables ────────────────────────────
# Assignment means putting value INTO a variable

# Integer (whole numbers)
# Why: Counting things (age, score, count)
age = 16
score = 100

# String (text)
# Why: Names, messages, text information
name = "Harshi"
city = "Bangalore"

# Float (decimal numbers)
# Why: Measurements, precise values (height, temperature)
height = 5.8
price = 99.99

# Boolean (True or False)
# Why: Yes/No decisions (is_student, is_logged_in)
is_student = True
is_rich = False

print(f"Age: {age}")
print(f"Name: {name}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# ── PART 2: Checking Variable Type ────────────────────────────
# Why: Sometimes you need to know what type of data you have

print("\nData Types:")
print(f"age is: {type(age)}")  # <class 'int'>
print(f"name is: {type(name)}")  # <class 'str'>
print(f"height is: {type(height)}")  # <class 'float'>
print(f"is_student is: {type(is_student)}")  # <class 'bool'>

# ── PART 3: Modifying Variables ────────────────────────────
# Why: Data changes, variables should too

age = age + 1  # Birthday! Age increases by 1
print(f"\nAfter birthday, age: {age}")

name = name + " Singh"  # Add last name
print(f"Full name: {name}")

# ── PART 4: Type Conversion ────────────────────────────
# Why: Sometimes you need to convert one type to another

string_number = "42"  # This is text that looks like a number
print(f"\nString number: {string_number}, Type: {type(string_number)}")

actual_number = int(string_number)  # Convert text to number
print(f"Actual number: {actual_number}, Type: {type(actual_number)}")

# Convert to string
number_to_string = str(123)  # Convert number to text
print(f"Number as string: {number_to_string}, Type: {type(number_to_string)}")

# Convert to float
age_float = float(age)  # Convert int to decimal
print(f"Age as float: {age_float}, Type: {type(age_float)}")

# ── PART 5: Multiple Assignment ────────────────────────────
# Why: Assign multiple variables in one line

a, b, c = 10, 20, 30
print(f"\nMultiple assignment: a={a}, b={b}, c={c}")

# Swap variables (interesting trick!)
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x  # Swap values
print(f"After swap: x={x}, y={y}")

# ── PART 6: Variable Naming Rules ────────────────────────────
# These are VALID variable names:
valid_name = "Can have underscores"
name2 = "Can have numbers at end"
_private = "Can start with underscore"
CONSTANT = "Can be all caps (by convention)"

# These are INVALID (don't use):
# 2name = "Can't start with number"
# name-with-dash = "Can't use dashes"
# name with space = "Can't use spaces"

print("\n✓ All valid variable names created successfully")

# ── Test Your Understanding ────────────────────────────
print("\n" + "="*50)
print("QUICK QUIZ")
print("="*50)

# 1. Create a variable with your name
my_name = "Harshi"
print(f"My name is {my_name}")

# 2. Create a variable with your age
my_age = 16
print(f"I am {my_age} years old")

# 3. Check the type of my_age
print(f"Type of my_age: {type(my_age)}")

# 4. Convert your age to string
age_string = str(my_age)
print(f"Age as text: {age_string}, Type: {type(age_string)}")

# 5. Create and modify a variable
score = 0
score = score + 50
score = score + 25
print(f"Final score: {score}")

print("\n✓ Complete Phase 1.1 to understand variables!")
