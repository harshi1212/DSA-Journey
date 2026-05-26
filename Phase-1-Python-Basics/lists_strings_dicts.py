"""
TOPIC: Lists, Strings, and Dictionaries
Difficulty: Beginner

These are the DATA STRUCTURES you'll use in every DSA problem.
Why: Storing and organizing data is 80% of programming.
"""

# ── PART 1: Lists ────────────────────────────
# A list is an ordered collection of items
# Why: Instead of: age1=10, age2=11, age3=12... use a list!

print("=== LISTS ===\n")

# Create a list
# Why: Group related data together
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True]  # Lists can have different types!

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# Access items by index (position)
# Why: Get a specific item from the list
# Remember: Indexing starts at 0!
first_fruit = fruits[0]  # Position 0 = first item
second_fruit = fruits[1]  # Position 1 = second item
print(f"\nFirst fruit: {first_fruit}")
print(f"Second fruit: {second_fruit}")

# Negative indexing (count from end)
# Why: Sometimes easier to count from end
last_fruit = fruits[-1]  # Last item
second_last = fruits[-2]  # Second-to-last
print(f"Last fruit: {last_fruit}")
print(f"Second-to-last: {second_last}")

# List length
# Why: How many items in list?
length = len(fruits)
print(f"\nLength of fruits: {length}")

# Add item to list
# Why: Data grows over time
fruits.append("date")  # Add to end
print(f"After append: {fruits}")

# Insert at specific position
# Why: Insert in middle, not just end
fruits.insert(1, "blueberry")  # Insert at position 1
print(f"After insert: {fruits}")

# Remove item
# Why: Delete something you don't want
fruits.remove("banana")  # Remove specific item
print(f"After remove: {fruits}")

# Pop (remove and get)
# Why: Remove item and use its value
last = fruits.pop()  # Remove last item
print(f"Popped: {last}")
print(f"After pop: {fruits}")

# Loop through list
# Why: Process each item
print("\nLoop through list:")
for fruit in fruits:
    print(f"- {fruit}")

# Slice a list
# Why: Get a portion of list
# Syntax: list[start:stop] (stop is NOT included)
numbers = [10, 20, 30, 40, 50]
first_three = numbers[0:3]  # Items at index 0, 1, 2
print(f"\nFirst three numbers: {first_three}")

middle = numbers[1:4]  # Items at index 1, 2, 3
print(f"Middle numbers: {middle}")

# List comprehension (advanced, but useful!)
# Why: Create new list from existing list elegantly
squared = [x*x for x in numbers]  # Square each number
print(f"Squared: {squared}")

evens = [x for x in numbers if x % 2 == 0]  # Only evens
print(f"Even numbers: {evens}")

# ── PART 2: Strings ────────────────────────────
# A string is text data
# Why: Names, messages, any text information

print("\n=== STRINGS ===\n")

# Create strings
name = "Harshi"
message = "Learning DSA is fun!"
empty = ""

print(f"Name: {name}")
print(f"Message: {message}")

# Strings are like lists of characters!
# Why: Can access individual characters
first_char = name[0]  # 'H'
last_char = name[-1]  # 'i'
print(f"\nFirst char: {first_char}")
print(f"Last char: {last_char}")

# String length
# Why: How many characters?
length = len(name)
print(f"Length of '{name}': {length}")

# Concatenation (joining strings)
# Why: Combine multiple strings
greeting = "Hello, " + name + "!"
print(f"Greeting: {greeting}")

first_name = "Harshi"
last_name = "Singh"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# String slicing
# Why: Get part of string
text = "PYTHON"
first_two = text[0:2]  # "PY"
middle = text[2:4]  # "TH"
print(f"\nFirst two chars: {first_two}")
print(f"Middle: {middle}")

# Useful string methods
# Why: Strings have built-in operations

text = "  Hello World  "
print(f"\nOriginal: '{text}'")
print(f"Stripped: '{text.strip()}'")  # Remove whitespace
print(f"Lowercase: '{text.lower()}'")  # Convert to lowercase
print(f"Uppercase: '{text.upper()}'")  # Convert to uppercase

text2 = "I love coding"
print(f"Replace: '{text2.replace('coding', 'DSA')}'")  # Replace text
print(f"Split: {text2.split()}")  # Split into words

# Find character in string
# Why: Is this character in the string?
word = "PYTHON"
if 'Y' in word:
    print(f"\n'Y' is in '{word}'")
if 'Z' not in word:
    print(f"'Z' is not in '{word}'")

# ── PART 3: Dictionaries ────────────────────────────
# A dictionary stores KEY → VALUE pairs
# Why: Look up information by key (like a real dictionary)

print("\n=== DICTIONARIES ===\n")

# Create dictionary
# Why: Store related data with meaningful names
student = {
    "name": "Harshi",
    "age": 16,
    "city": "Bangalore",
    "is_coder": True
}

print(f"Student: {student}")

# Access value by key
# Why: Get information using descriptive key
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"City: {student['city']}")

# Check if key exists
# Why: Avoid errors when accessing missing key
if "name" in student:
    print("\nName key exists")

if "phone" not in student:
    print("Phone key doesn't exist")

# Add new key-value pair
# Why: Add new information
student["phone"] = "9876543210"
print(f"\nAfter adding phone: {student}")

# Update existing value
# Why: Information changes
student["age"] = 17
print(f"After updating age: {student}")

# Delete key-value pair
# Why: Remove information
del student["phone"]
print(f"After deleting phone: {student}")

# Get all keys
# Why: Iterate through dictionary
print("\nAll keys:")
for key in student:
    print(f"- {key}")

# Get all values
# Why: List all information
print("\nAll values:")
for value in student.values():
    print(f"- {value}")

# Get key-value pairs
# Why: Work with both key and value
print("\nKey-value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary with default value
# Why: Get value safely even if key doesn't exist
score = student.get("score", 0)  # If "score" doesn't exist, use 0
print(f"\nScore (with default): {score}")

# ── PART 4: Choosing the Right Data Structure ────────────────────────────

print("\n=== WHEN TO USE WHAT ===\n")

# Use LIST when:
# - Order matters
# - Items can repeat
# - You access by position

to_buy = ["milk", "bread", "eggs"]  # Order matters when shopping
print(f"Shopping list: {to_buy}")

# Use SET when:
# - No duplicates allowed
# - Order doesn't matter
# - Check membership fast

numbers_set = {1, 2, 3, 4, 5}
if 3 in numbers_set:
    print("3 is in the set")

# Use DICTIONARY when:
# - Fast lookup by key
# - Group related data
# - Descriptive access

person = {"name": "Harshi", "age": 16, "hobby": "coding"}
print(f"Person's hobby: {person['hobby']}")

# ── Test Your Understanding ────────────────────────────
print("\n" + "="*50)
print("QUICK QUIZ")
print("="*50)

# 1. Create list, add items, access them
my_list = [10, 20, 30]
my_list.append(40)
print(f"\n1. List: {my_list}")
print(f"   Third item: {my_list[2]}")

# 2. String operations
word = "HARSHI"
print(f"\n2. Word: {word}")
print(f"   Length: {len(word)}")
print(f"   First 3 chars: {word[0:3]}")
print(f"   Lowercase: {word.lower()}")

# 3. Dictionary operations
book = {"title": "DSA Guide", "pages": 500, "author": "You"}
print(f"\n3. Book: {book}")
print(f"   Title: {book['title']}")
print(f"   Pages: {book['pages']}")
book["rating"] = 5
print(f"   After adding rating: {book}")

print("\n✓ Complete Phase 1.4 to master data structures!")
