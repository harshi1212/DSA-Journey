"""
TOPIC: Loops - FOR and WHILE
Difficulty: Beginner

Loops let you repeat code without copy-pasting.
Why: If you want to print something 1000 times, write a loop!
"""

# ── PART 1: FOR Loops ────────────────────────────
# FOR loop: "For each item, do this"
# Why: You know exactly what to loop through

print("=== FOR LOOPS ===\n")

# Example 1: Count from 0 to 4
# Why: Simple repetition
print("Counting 0 to 4:")
for i in range(5):  # range(5) = [0, 1, 2, 3, 4]
    # This line runs 5 times
    print(f"Number: {i}")

# Example 2: Loop through a list
# Why: Do something with each item in a list
print("\nLoop through list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    # This runs once for each fruit in the list
    print(f"I like {fruit}")

# Example 3: Loop with range(start, stop, step)
# Why: Control exactly what numbers to loop through
print("\nCount by 2s from 0 to 8:")
for i in range(0, 10, 2):  # Start at 0, stop before 10, step by 2
    print(i)

# Example 4: Nested loops (loop inside loop)
# Why: When you need multiple levels of repetition
print("\nMultiplication table (3x3):")
for i in range(1, 4):  # Row: 1, 2, 3
    for j in range(1, 4):  # Column: 1, 2, 3
        # This runs 3x3 = 9 times
        product = i * j
        print(f"{i}×{j}={product}", end=" ")
    print()  # Newline after each row

# Example 5: Loop through string
# Why: Strings are lists of characters
print("\nLoop through word:")
word = "HARSHI"
for letter in word:
    # This runs once for each letter
    print(letter, end="-")
print()

# ── PART 2: WHILE Loops ────────────────────────────
# WHILE loop: "While this is true, keep doing this"
# Why: You don't know how many times to loop

print("\n=== WHILE LOOPS ===\n")

# Example 1: Simple countdown
# Why: Repeat until condition becomes False
print("Countdown from 3 to 1:")
count = 3
while count > 0:
    # This runs as long as count > 0 is True
    print(count)
    count = count - 1  # MUST update count, or infinite loop!
print("Blastoff! 🚀")

# Example 2: Repeat until input is correct
# Why: Real-world: validate user input until correct
print("\nGuess the number (it's 7):")
guess = -1
tries = 0
while guess != 7:
    # Keep looping until guess is 7
    guess = int(input("Enter number: "))
    tries = tries + 1
    if guess < 7:
        print("Too low!")
    elif guess > 7:
        print("Too high!")
    else:
        print(f"Correct! You took {tries} tries.")

# Example 3: Process data until condition met
# Why: Common pattern in real programs
print("\nFinding first number greater than 50:")
power_of_2 = 1
while power_of_2 <= 50:
    # Keep doubling until we exceed 50
    power_of_2 = power_of_2 * 2
print(f"First power of 2 > 50 is: {power_of_2}")

# ── PART 3: Loop Control ────────────────────────────
# BREAK: Exit loop immediately
# Why: Stop looping when you find what you're looking for

print("\n=== LOOP CONTROL ===\n")

print("Find 'c' in alphabet:")
for letter in "abcdefgh":
    if letter == "c":
        print(f"Found: {letter}")
        break  # Exit loop, don't check rest
    print(letter, end=" ")
print("\nLoop ended")

# CONTINUE: Skip current iteration, go to next
# Why: Skip items you don't want to process

print("\nPrint even numbers only (skip odd):")
for i in range(1, 6):
    if i % 2 == 1:  # If odd
        continue  # Skip this number, go to next
    print(i)  # Only even numbers print

# ── PART 4: Loop with Index ────────────────────────────
# Why: Sometimes you need both the item AND its position

print("\n=== LOOP WITH INDEX ===\n")

fruits = ["apple", "banana", "cherry"]
for index in range(len(fruits)):
    # len() gives length, range() creates indices 0,1,2...
    fruit = fruits[index]
    print(f"Position {index}: {fruit}")

# Better way: enumerate()
# Why: Gets index AND item automatically
print("\nUsing enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Position {index}: {fruit}")

# ── PART 5: Loop Patterns (Important!) ────────────────────────────
# These patterns appear in almost every DSA problem

print("\n=== COMMON LOOP PATTERNS ===\n")

# Pattern 1: Sum all items
# Why: Calculate total
numbers = [1, 2, 3, 4, 5]
total = 0  # Start with 0
for num in numbers:
    total = total + num  # Add each number
print(f"Sum of {numbers} = {total}")

# Pattern 2: Count items that match condition
# Why: How many match a criteria?
count = 0  # Start with 0
for num in numbers:
    if num > 2:  # If number is greater than 2
        count = count + 1  # Increase count
print(f"Numbers > 2: {count}")

# Pattern 3: Find maximum value
# Why: What's the largest?
max_num = numbers[0]  # Start with first item
for num in numbers:
    if num > max_num:  # If current is bigger
        max_num = num  # Update max
print(f"Maximum: {max_num}")

# Pattern 4: Build a new list (transformation)
# Why: Create new list from old one
squared = []  # Start empty
for num in numbers:
    squared.append(num * num)  # Add squared value
print(f"Squares: {squared}")

# ── Test Your Understanding ────────────────────────────
print("\n" + "="*50)
print("QUICK QUIZ")
print("="*50)

# 1. Print numbers 1 to 5
print("\n1. Numbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# 2. Print first 3 characters of a word
word = "PYTHON"
print(f"\n2. First 3 chars of {word}:")
for i in range(3):
    print(word[i], end="")
print()

# 3. Count even numbers from 1 to 10
even_count = 0
for i in range(1, 11):
    if i % 2 == 0:
        even_count = even_count + 1
print(f"\n3. Even numbers from 1 to 10: {even_count}")

print("\n✓ Complete Phase 1.2 to master loops!")
