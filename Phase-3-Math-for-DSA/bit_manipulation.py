"""
TOPIC: Bit Manipulation
Difficulty: Beginner-Intermediate

Bits are the 0s and 1s of binary numbers.
Why: Optimize space and speed, solve tricky problems elegantly.
"""

print("=== BIT MANIPULATION ===\n")

# View binary representation
# Why: Understand bit operations
print("Binary Representation:")
for num in [5, 10, 15, 255]:
    print(f"{num:3} = {bin(num)}")

print()

# Bitwise AND (&)
# Why: Check if bit is set, common pattern
print("Bitwise AND (&) - Both bits must be 1:")
print(f"5 & 3 = {5 & 3}")  # 101 & 011 = 001 = 1
print(f"6 & 5 = {6 & 5}")  # 110 & 101 = 100 = 4

# Check if odd (last bit is 1)
# Why: Very common pattern
num = 7
if num & 1:
    print(f"{num} is odd")

# Bitwise OR (|)
# Why: Set a bit to 1
print("\nBitwise OR (|) - At least one bit is 1:")
print(f"5 | 3 = {5 | 3}")  # 101 | 011 = 111 = 7
print(f"4 | 2 = {4 | 2}")  # 100 | 010 = 110 = 6

# Bitwise XOR (^)
# Why: Toggle a bit, find unique elements
print("\nBitwise XOR (^) - Bits are different:")
print(f"5 ^ 3 = {5 ^ 3}")  # 101 ^ 011 = 110 = 6
print(f"5 ^ 5 = {5 ^ 5}")  # 101 ^ 101 = 000 = 0 (XOR with self = 0)

# XOR trick: Find unique element
# Why: XOR of all elements except one will be that element
numbers = [1, 2, 2, 3, 3, 4, 4]
unique = 0
for num in numbers:
    unique ^= num
print(f"\nUnique element in {numbers}: {unique}")

# Bitwise NOT (~)
# Why: Invert all bits
print("\nBitwise NOT (~) - Invert all bits:")
print(f"~5 = {~5}")  # In Python, this is -(5+1) = -6

# Left Shift (<<)
# Why: Multiply by 2^n, very fast
print("\nLeft Shift (<<) - Multiply by 2^n:")
print(f"5 << 1 = {5 << 1}")  # 101 << 1 = 1010 = 10 (multiply by 2)
print(f"5 << 2 = {5 << 2}")  # 101 << 2 = 10100 = 20 (multiply by 4)
print(f"3 << 3 = {3 << 3}")  # 11 << 3 = 11000 = 24 (multiply by 8)

# Right Shift (>>)
# Why: Divide by 2^n, very fast
print("\nRight Shift (>>) - Divide by 2^n:")
print(f"16 >> 1 = {16 >> 1}")  # 10000 >> 1 = 1000 = 8 (divide by 2)
print(f"20 >> 2 = {20 >> 2}")  # 10100 >> 2 = 101 = 5 (divide by 4)

# Count Set Bits (number of 1s in binary)
# Why: Useful for many problems
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1  # Check if last bit is 1
        n >>= 1         # Right shift to check next bit
    return count

print("\nCount Set Bits (number of 1s):")
test_nums = [5, 10, 15, 255]
for num in test_nums:
    bits = count_set_bits(num)
    print(f"{num} ({bin(num)}): {bits} set bits")

# Efficient set bit counter
print("\nBuilt-in set bit counter:")
print(f"bin(13).count('1') = {bin(13).count('1')}")

# Power of 2 check
# Why: Common interview question
def is_power_of_2(n):
    # Power of 2 has exactly one set bit
    # n & (n-1) clears the lowest set bit
    # If result is 0, only one bit was set
    return n > 0 and (n & (n - 1)) == 0

print("\nPower of 2 Check:")
test_nums = [1, 2, 4, 8, 16, 5, 10, 15]
for num in test_nums:
    print(f"{num}: {is_power_of_2(num)}", end=" | ")
print()

# Set/Clear specific bit
# Why: Manipulate individual flags
def set_bit(num, position):
    return num | (1 << position)

def clear_bit(num, position):
    return num & ~(1 << position)

def toggle_bit(num, position):
    return num ^ (1 << position)

print("\nSet/Clear/Toggle Bit:")
num = 5  # 101
print(f"Original: {num} ({bin(num)})")
print(f"Set bit 1: {set_bit(num, 1)} ({bin(set_bit(num, 1))})")
print(f"Clear bit 0: {clear_bit(num, 0)} ({bin(clear_bit(num, 0))})")
print(f"Toggle bit 2: {toggle_bit(num, 2)} ({bin(toggle_bit(num, 2))})")
