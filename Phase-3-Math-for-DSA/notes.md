# Phase 3 - Mathematics for DSA

## What is it?

DSA uses some math concepts frequently. You don't need to be a math genius, but you need to understand:
- **Modulo** → Remainder after division (used in hashing, circular arrays)
- **Primes** → Numbers divisible only by 1 and themselves (used in hashing)
- **Bit manipulation** → Working with binary (used in optimization tricks)
- **GCD/LCM** → Greatest common divisor (used in problems)

These aren't calculus or algebra—they're practical tools for algorithms.

---

## Why does it matter?

**Real-world reasons:**
1. **Hash tables** - Modulo determines bucket position
2. **Cryptography** - Prime numbers are security foundation
3. **Optimization** - Bit tricks make code 10x faster
4. **Interview questions** - "Count set bits", "Find prime factors"
5. **Competitive programming** - Math tricks solve problems elegantly

---

## How to think about it

```
Modulo: 17 ÷ 5 = 3 remainder 2  →  17 % 5 = 2
Primes: Only divisible by 1 and itself  →  2, 3, 5, 7, 11, 13...
Bits: Store multiple flags in single number  →  110 (6 in decimal)
GCD: Largest number dividing both  →  GCD(12, 18) = 6
```

---

## Python Implementation

### Modulo

```python
# Modulo (%) gives remainder
# Why: Very common in DSA

print("MODULO")
print(17 % 5)  # 17 = 3×5 + 2, so remainder is 2 → 2
print(10 % 3)  # 10 = 3×3 + 1, so remainder is 1 → 1
print(20 % 4)  # 20 = 5×4 + 0, so remainder is 0 → 0

# Use case: Check even/odd
# Why: A number is even if divided by 2 has remainder 0
number = 10
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Use case: Circular indexing
# Why: When you reach end, go back to start
position = 27
array_size = 10
circular_position = position % array_size  # 27 % 10 = 7
print(f"Position 27 in array of 10 → index {circular_position}")
```

### Primes

```python
# Check if number is prime
# Why: Primes are used in many algorithms

def is_prime(n):
    # A prime is only divisible by 1 and itself
    if n < 2:
        return False
    
    # Check divisibility from 2 to sqrt(n)
    # Why: If n = a×b, one of a or b must be ≤ sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

# Test primes
print(f"Is 7 prime? {is_prime(7)}")      # True
print(f"Is 10 prime? {is_prime(10)}")    # False
print(f"Is 17 prime? {is_prime(17)}")    # True

# Find all primes up to n (Sieve of Eratosthenes)
def sieve_of_eratosthenes(n):
    # Mark all as prime initially
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    # Mark multiples of primes as not prime
    for i in range(2, int(n**0.5) + 1):
        if is_prime_arr[i]:
            for j in range(i*i, n + 1, i):
                is_prime_arr[j] = False
    
    # Return only primes
    return [i for i in range(n + 1) if is_prime_arr[i]]

primes = sieve_of_eratosthenes(20)
print(f"Primes up to 20: {primes}")
```

### Bit Manipulation

```python
# Work with binary representations
# Why: Optimize space and speed

# Binary basics
print("BITS")
print(f"5 in binary: {bin(5)}")    # 0b101 (3 bits: 1 0 1)
print(f"10 in binary: {bin(10)}")  # 0b1010

# Bitwise AND (&)
# Why: Check if bit is set
print(f"5 & 1 = {5 & 1}")   # Check if 5 is odd
print(f"6 & 1 = {6 & 1}")   # Check if 6 is odd

# Bitwise OR (|)
# Why: Set a bit
print(f"4 | 2 = {4 | 2}")   # 4 (100) | 2 (010) = 6 (110)

# Bitwise XOR (^)
# Why: Toggle a bit, or find unique element
print(f"5 ^ 3 = {5 ^ 3}")

# Left shift (<<)
# Why: Multiply by 2^n
print(f"5 << 1 = {5 << 1}")   # 5 * 2 = 10

# Right shift (>>)
# Why: Divide by 2^n
print(f"10 >> 1 = {10 >> 1}")  # 10 / 2 = 5

# Count set bits (number of 1s in binary)
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1  # Check if last bit is 1
        n >>= 1         # Right shift to check next bit
    return count

print(f"Set bits in 5: {count_set_bits(5)}")   # 5 = 101, two 1s
print(f"Set bits in 10: {count_set_bits(10)}")  # 10 = 1010, two 1s
```

### GCD and LCM

```python
# Greatest Common Divisor
# Why: Find largest number dividing both

import math

# Using Python's built-in
gcd = math.gcd(12, 18)
print(f"GCD(12, 18) = {gcd}")  # 6

# Euclidean algorithm (how it works)
def gcd_manual(a, b):
    while b:
        # Key insight: GCD(a,b) = GCD(b, a%b)
        a, b = b, a % b
    return a

print(f"GCD(12, 18) manual = {gcd_manual(12, 18)}")

# Least Common Multiple
# Why: Find smallest number divisible by both

def lcm(a, b):
    # LCM × GCD = a × b
    return (a * b) // gcd_manual(a, b)

print(f"LCM(12, 18) = {lcm(12, 18)}")  # 36
```

---

## Common Mistakes Beginners Make

1. **Confusing % with division**
   - ❌ Wrong: `17 % 5` gives 17/5 = 3.4
   - ✅ Right: `17 % 5 = 2` (the remainder)

2. **Inefficient prime checking**
   - ❌ Wrong: Check divisibility up to n
   - ✅ Right: Check only up to sqrt(n)

3. **Bit operations on negative numbers**
   - ❌ Wrong: Not considering two's complement in Python
   - ✅ Right: Use proper bit operations

4. **Slow bit counting**
   - ❌ Wrong: Manual loop when Python has bin().count('1')
   - ✅ Right: Use efficient methods

5. **Forgetting operator precedence**
   - ❌ Wrong: `5 + 3 << 1` (what order?)
   - ✅ Right: Use parentheses: `(5 + 3) << 1`

6. **Integer overflow (less relevant in Python)**
   - ❌ Wrong: Large bit shifts without checking bounds
   - ✅ Right: Verify range of operations

---

## How to know I understand this

Checklist:
- [ ] I can explain modulo with an example
- [ ] I can check if a number is prime in < 1 minute
- [ ] I can count set bits using bitwise operations
- [ ] I can find GCD of two numbers
- [ ] I understand why bit operations are fast
- [ ] I can solve an easy "bit" LeetCode problem

---

## Practice Problems

- Easy: [Check if Number is Even or Odd — LeetCode #2469](https://leetcode.com/problems/convert-the-temperature/)
- Easy: [Single Number — LeetCode #136](https://leetcode.com/problems/single-number/)
- Easy: [Number of 1 Bits — LeetCode #191](https://leetcode.com/problems/number-of-1-bits/)
- Medium: [Prime Number of Set Bits — LeetCode #762](https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/)
