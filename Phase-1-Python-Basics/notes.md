# Phase 1 - Python Basics

## What is it?

Python basics are like learning the alphabet before writing poems. You need to know:
- **Variables** → Containers that hold information (like labeled boxes)
- **Data types** → What kind of information (numbers, text, yes/no)
- **Loops** → Repeating actions without copying code 100 times
- **Functions** → Reusable blocks of code (like recipes you use multiple times)
- **Lists & Dictionaries** → Storing multiple things organized

Think of Python as a simple conversation with your computer:
```
You: "Save 10 in a container called age"
Computer: "Done."
You: "Print age"
Computer: "10"
```

---

## Why does it matter?

**Real-world reasons:**
1. **Every program starts here** - You can't build anything without understanding variables and loops
2. **Interview questions** - "Write a function to..." starts with function basics
3. **DSA is just Python** - All our algorithms are written in these fundamentals
4. **Reading code** - You need to understand loops and functions to read other people's solutions
5. **Problem solving** - Variables hold state, loops process data, functions solve problems

---

## How to think about it

Your brain thinks about programming in this order:

```
Data (What do I store?)
   ↓
Variables (Where do I store it?)
   ↓
Data Types (What kind of data?)
   ↓
Operations (What can I do with it?)
   ↓
Functions (How do I organize operations?)
   ↓
Loops (How do I repeat operations?)
```

A program is just:
- Store data in variables
- Change data with operations
- Repeat with loops
- Organize with functions

---

## Python Implementation

### 1. Variables and Data Types

```python
# ── Variables ────────────────────────────────
# A variable is a named container for storing information
# Think of it like a labeled box

# Creating variables (assignment)
# Why: We need somewhere to store data
age = 16  # "age" is the variable name, 16 is the value
name = "Harshi"  # Text data (called a string)
height = 5.8  # Decimal numbers (called float)
is_learning = True  # Yes/No data (called boolean)

# Why each data type exists:
# - int: for counting (age, score, quantity)
# - float: for measurements (height, temperature, price)
# - str: for text (name, message, filename)
# - bool: for yes/no (is_student, is_logged_in)

print(f"Name: {name}, Age: {age}, Height: {height}m, Learning: {is_learning}")
# Output: Name: Harshi, Age: 16, Height: 5.8m, Learning: True

# Checking data type
# Why: Sometimes you need to know what type of data you have
print(type(age))  # <class 'int'>
print(type(name))  # <class 'str'>
```

### 2. Loops - Repeating code without copy-paste

```python
# ── Loops ────────────────────────────────
# A loop runs the same code multiple times
# Why: Never copy-paste code. Loop instead.

# FOR loop - when you know exactly how many times to repeat
# Why: Perfect for "do this 5 times" or "for each item in a list"
print("--- FOR LOOP ---")
for i in range(5):  # range(5) means 0, 1, 2, 3, 4
    # This line runs 5 times
    print(f"Count: {i}")

# Output:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4

# Loop through a list
# Why: You have 5 students, print each name. Don't write 5 print statements!
students = ["Alice", "Bob", "Charlie"]
for student in students:
    # This runs once for each student
    print(f"Hello {student}")

# WHILE loop - when you don't know how many times
# Why: "Repeat until this condition is False"
print("\n--- WHILE LOOP ---")
count = 0
while count < 3:  # "While count is less than 3..."
    # This runs as long as condition is True
    print(f"Count is {count}")
    count = count + 1  # Must update count, or loop runs forever!

# Output:
# Count is 0
# Count is 1
# Count is 2
```

### 3. Functions - Reusable code blocks

```python
# ── Functions ────────────────────────────────
# A function is code you write once and use many times
# Why: Don't repeat code. Write once, call many times.

# Basic function
# Why: Organize related operations together
def greet():
    # This is the function body (indented code)
    print("Hello! Welcome to DSA learning!")

# Call the function
# Why: Whenever you need this code, just call the function
greet()
greet()
greet()

# Output runs 3 times:
# Hello! Welcome to DSA learning!
# Hello! Welcome to DSA learning!
# Hello! Welcome to DSA learning!

# Function with parameters (inputs)
# Why: Same function, different data
def add(a, b):
    # a and b are parameters (inputs)
    # The code inside uses these values
    result = a + b
    return result  # Send the answer back to whoever called this function

# Call function with arguments
answer = add(10, 20)  # 10 and 20 are arguments (actual values)
print(f"10 + 20 = {answer}")  # Output: 10 + 20 = 30

# Function to check if a number is even
# Why: Common operation, let's make it reusable
def is_even(number):
    # If number divided by 2 has no remainder, it's even
    if number % 2 == 0:
        return True
    else:
        return False

# Test it
print(is_even(10))  # True (10 is even)
print(is_even(7))   # False (7 is odd)
```

### 4. Lists and Dictionaries

```python
# ── Lists ────────────────────────────────
# A list stores multiple items in order
# Why: Instead of age1=10, age2=11, age3=12... use a list!

ages = [10, 11, 12, 13, 14]  # Created a list with 5 numbers
print(ages)  # [10, 11, 12, 13, 14]

# Access items by position (index)
# Why: Sometimes you need the 1st item, 3rd item, etc.
# Important: Indexing starts at 0!
first = ages[0]  # Get item at position 0 (first item)
print(f"First age: {first}")  # 10

third = ages[2]  # Get item at position 2 (third item)
print(f"Third age: {third}")  # 12

# Add item to list
# Why: Data changes, lists should too
ages.append(15)  # Add 15 to the end
print(ages)  # [10, 11, 12, 13, 14, 15]

# Remove item
# Why: You made a mistake, remove it
ages.remove(11)  # Remove the number 11
print(ages)  # [10, 12, 13, 14, 15]

# Loop through a list
# Why: Do something with each item
print("All ages:")
for age in ages:
    print(f"Age: {age}")

# ── Dictionaries ────────────────────────────────
# A dictionary stores pairs: KEY → VALUE
# Why: "What is the phone number of Harshi?" 
# Instead of multiple variables, use a dictionary!

person = {
    "name": "Harshi",      # Key: "name", Value: "Harshi"
    "age": 16,             # Key: "age", Value: 16
    "city": "Bangalore",   # Key: "city", Value: "Bangalore"
}

# Access values using keys
# Why: Look up any information instantly
print(person["name"])  # "Harshi"
print(person["age"])   # 16

# Add new key-value pair
# Why: Collect more information about the person
person["hobby"] = "Coding"  # Add new key
print(person)

# Update existing value
# Why: Information changes
person["age"] = 17  # Update age to 17

# Loop through dictionary
# Why: Do something with each pair
print("Person info:")
for key in person:
    value = person[key]
    print(f"{key}: {value}")
```

---

## Common Mistakes Beginners Make

1. **Using undefined variables**
   - ❌ Wrong: `print(x)` without first doing `x = 5`
   - ✅ Right: Always define before using

2. **Forgetting the colon `:` after function and loop definitions**
   - ❌ Wrong: `def add(a, b)` and `for i in range(5)`
   - ✅ Right: `def add(a, b):` and `for i in range(5):`

3. **Not indenting code inside loops and functions**
   - ❌ Wrong: Code not aligned properly after `:` is not part of the block
   - ✅ Right: All code inside should be indented (4 spaces or 1 Tab)

4. **Confusing = (assignment) with == (comparison)**
   - ❌ Wrong: `if x = 5:` sets x to 5, doesn't check equality
   - ✅ Right: `if x == 5:` checks if x equals 5

5. **Index out of range in lists**
   - ❌ Wrong: `list[10]` when list only has 5 items (indices 0-4)
   - ✅ Right: Check list length first with `len(list)` or use loops

6. **Infinite while loops**
   - ❌ Wrong: `while True: print("hi")` - never ends!
   - ✅ Right: Always update the condition: `while count < 10: count += 1`

---

## How to know I understand this

Checklist:
- [ ] I can explain variables, loops, and functions without looking at notes
- [ ] I can write a function that takes 2 inputs and returns a result in 5 minutes
- [ ] I can loop through a list and modify each item
- [ ] I understand when to use for loops vs while loops
- [ ] I can create a dictionary and access values by key
- [ ] I can solve an easy LeetCode problem using these basics

---

## Practice Problems

- Easy: [Two Sum — LeetCode #1](https://leetcode.com/problems/two-sum/)
- Easy: [Palindrome Number — LeetCode #9](https://leetcode.com/problems/palindrome-number/)
- Easy: [Reverse String — LeetCode #344](https://leetcode.com/problems/reverse-string/)
- Medium: [Majority Element — LeetCode #169](https://leetcode.com/problems/majority-element/)
- Medium: [First Missing Positive — LeetCode #41](https://leetcode.com/problems/first-missing-positive/)
