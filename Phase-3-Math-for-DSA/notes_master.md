# Phase 3 - Math for DSA (Complete Master Guide)

**Mathematically solve problems. Numbers appear in 30% of DSA interviews.**

---

## Table of Contents
1. [Number System Foundations](#number-system-foundations)
2. [Modular Arithmetic](#modular-arithmetic)
3. [Prime Numbers](#prime-numbers)
4. [GCD and LCM](#gcd-and-lcm)
5. [Bit Manipulation](#bit-manipulation)
6. [Combinatorics](#combinatorics)
7. [Number Theory](#number-theory)
8. [Worked Examples (50+)](#worked-examples)
9. [Interview Preparation](#interview-preparation)

---

# NUMBER SYSTEM FOUNDATIONS

## Number Bases

**Definition:** A number base (or radix) is the number of unique digits used in a positional numeral system.

### Decimal (Base 10)

```python
# 1234₁₀ = 1×10³ + 2×10² + 3×10¹ + 4×10⁰
#        = 1000 + 200 + 30 + 4

num = 1234
print(num)  # 1234
```

### Binary (Base 2)

```python
# 1011₂ = 1×2³ + 0×2² + 1×2¹ + 1×2⁰
#       = 8 + 0 + 2 + 1 = 11₁₀

# Decimal to binary:
num = 11
binary = bin(num)        # '0b1011'
binary_str = bin(num)[2:]  # '1011'

# Binary to decimal:
binary_num = 0b1011
decimal = int('1011', 2)  # 11
```

### Hexadecimal (Base 16)

```python
# Digits: 0-9, A(10)-F(15)
# FF₁₆ = 15×16¹ + 15×16⁰ = 240 + 15 = 255₁₀

# Decimal to hex:
num = 255
hex_str = hex(num)  # '0xff'

# Hex to decimal:
hex_num = 0xFF
decimal = int('FF', 16)  # 255
```

---

## Base Conversion Algorithm

```python
def decimal_to_base(num, base):
    """Convert decimal number to any base (2-36)"""
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while num:
        result = digits[num % base] + result
        num //= base
    
    return result

def base_to_decimal(num_str, base):
    """Convert number from any base (2-36) to decimal"""
    result = 0
    
    for digit in num_str:
        result = result * base + int(digit, base)
    
    return result

# Examples:
print(decimal_to_base(255, 2))   # "11111111"
print(decimal_to_base(255, 16))  # "FF"
print(base_to_decimal("1111", 2))  # 15
print(base_to_decimal("FF", 16))   # 255
```

---

# MODULAR ARITHMETIC

## Modulo Operation

**Definition:** $a \mod n$ is the remainder when $a$ is divided by $n$

$$a \equiv r \pmod{n} \text{ means } a = qn + r \text{ where } 0 \leq r < n$$

```python
# Examples:
print(17 % 5)   # 2  (17 = 3×5 + 2)
print(20 % 7)   # 6  (20 = 2×7 + 6)
print(15 % 15)  # 0  (15 = 1×15 + 0)
```

---

## Modular Arithmetic Properties

```python
# Property 1: (a + b) mod n = ((a mod n) + (b mod n)) mod n
a, b, n = 17, 13, 5
print((a + b) % n)                    # 0
print(((a % n) + (b % n)) % n)        # 0

# Property 2: (a × b) mod n = ((a mod n) × (b mod n)) mod n
print((a * b) % n)                    # 1
print(((a % n) * (b % n)) % n)        # 1

# Property 3: (a - b) mod n = ((a mod n) - (b mod n) + n) mod n
print((a - b) % n)                    # 4
print(((a % n) - (b % n) + n) % n)    # 4
```

---

## Modular Exponentiation

**Problem:** Compute $a^b \mod m$ efficiently (without overflow)

```python
def mod_exp(base, exp, mod):
    """
    Calculate base^exp mod mod efficiently
    
    Time: O(log exp)
    Space: O(1)
    """
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd
            result = (result * base) % mod
        
        exp = exp >> 1      # exp //= 2
        base = (base * base) % mod
    
    return result

# Example: 2^10 mod 1000
print(mod_exp(2, 10, 1000))  # 24

# Compare:
print(pow(2, 10) % 1000)     # 24 (Python built-in)
print(pow(2, 10, 1000))      # 24 (with modulo)
```

---

# PRIME NUMBERS

## Prime Number Definition

**Definition:** A prime number is a natural number > 1 that has no positive divisors other than 1 and itself.

```python
def is_prime_naive(n):
    """
    Check if n is prime (naive approach)
    
    Time: O(n)
    Space: O(1)
    """
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

# Time: O(√n) - only check up to square root
def is_prime(n):
    """
    Check if n is prime (optimized)
    
    Insight: If n = a×b and a > √n, then b < √n
    So we only need to check divisors up to √n
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Test:
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for p in primes:
    print(f"{p}: {is_prime(p)}")  # All True
```

---

## Sieve of Eratosthenes

**Problem:** Find all primes up to n efficiently

```python
def sieve_of_eratosthenes(n):
    """
    Find all primes up to n
    
    Time: O(n log log n)
    Space: O(n)
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as not prime
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # Collect all primes
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

# Example: Find primes up to 30
print(sieve_of_eratosthenes(30))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Visualization:
# Start: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]
# Mark 2: [2, 3, -, 5, -, 7, -, 9, -, 11, ...]
# Mark 3: [2, 3, -, 5, -, 7, -, -, -, 11, ...]
# Mark 5: [2, 3, -, 5, -, 7, -, -, -, 11, ...]
```

---

# GCD AND LCM

## Greatest Common Divisor (GCD)

**Definition:** The largest positive integer that divides both a and b

```python
def gcd(a, b):
    """
    Euclidean Algorithm for GCD
    
    Principle: gcd(a, b) = gcd(b, a mod b)
    
    Time: O(log min(a, b))
    Space: O(1)
    """
    while b:
        a, b = b, a % b
    return a

# Example: gcd(48, 18)
# 48 = 2 × 18 + 12
# 18 = 1 × 12 + 6
# 12 = 2 × 6 + 0
# GCD = 6

print(gcd(48, 18))  # 6

# Using built-in:
import math
print(math.gcd(48, 18))  # 6
```

---

## Least Common Multiple (LCM)

**Definition:** The smallest positive integer divisible by both a and b

**Formula:** $\text{LCM}(a, b) = \frac{a \times b}{\text{GCD}(a, b)}$

```python
def lcm(a, b):
    """
    Calculate LCM using GCD
    
    Time: O(log min(a, b))
    Space: O(1)
    """
    return (a * b) // gcd(a, b)

# Example: lcm(12, 18)
# GCD(12, 18) = 6
# LCM = (12 × 18) / 6 = 36

print(lcm(12, 18))  # 36

# Verification:
print(36 % 12)  # 0 (36 divisible by 12)
print(36 % 18)  # 0 (36 divisible by 18)
```

---

# BIT MANIPULATION

## Bit Basics

```python
# AND (&): Both bits must be 1
print(5 & 3)    # 5 = 101, 3 = 011 → 001 = 1

# OR (|): At least one bit is 1
print(5 | 3)    # 5 = 101, 3 = 011 → 111 = 7

# XOR (^): Bits must be different
print(5 ^ 3)    # 5 = 101, 3 = 011 → 110 = 6

# NOT (~): Flip all bits
print(~5)       # ~101 → ...11111010 (two's complement)

# Left shift (<<): Multiply by 2
print(5 << 1)   # 101 → 1010 = 10

# Right shift (>>): Divide by 2
print(5 >> 1)   # 101 → 10 = 2
```

---

## Common Bit Tricks

```python
# Check if number is power of 2
def is_power_of_2(n):
    """
    n is power of 2 if n & (n-1) == 0
    
    Why? Power of 2 has only 1 bit set
    n   = 1000
    n-1 = 0111
    n & (n-1) = 0000
    """
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_2(8))   # True (8 = 1000)
print(is_power_of_2(6))   # False (6 = 0110)

# Count number of set bits (1s)
def count_set_bits(n):
    """Count number of 1s in binary representation"""
    count = 0
    while n:
        count += n & 1  # Check if last bit is 1
        n >>= 1         # Shift right
    return count

print(count_set_bits(5))   # 2 (101 has two 1s)

# Find single number in array where all others appear twice
def find_single(nums):
    """
    XOR: a ^ a = 0, a ^ 0 = a
    So XORing all numbers leaves only the single one
    """
    result = 0
    for num in nums:
        result ^= num
    return result

print(find_single([1, 2, 2, 3, 3]))  # 1

# Check if bit at position i is set
def is_bit_set(num, i):
    return (num & (1 << i)) != 0

print(is_bit_set(5, 0))  # True (5 = 101, bit 0 is 1)
print(is_bit_set(5, 1))  # False (5 = 101, bit 1 is 0)

# Set bit at position i
def set_bit(num, i):
    return num | (1 << i)

print(set_bit(5, 1))  # 7 (101 → 111)

# Clear bit at position i
def clear_bit(num, i):
    return num & ~(1 << i)

print(clear_bit(5, 0))  # 4 (101 → 100)

# Toggle bit at position i
def toggle_bit(num, i):
    return num ^ (1 << i)

print(toggle_bit(5, 1))  # 7 (101 → 111)
```

---

# COMBINATORICS

## Permutations

**Definition:** Arrangement of n objects in specific order

$$P(n, r) = \frac{n!}{(n-r)!}$$

```python
import math

def permutations(n, r):
    """
    Calculate P(n, r) = n! / (n-r)!
    Time: O(r)
    Space: O(1)
    """
    if r > n or r < 0:
        return 0
    
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    
    return result

# Example: P(5, 2) = arrangements of 2 items from 5
# 5 × 4 = 20
print(permutations(5, 2))        # 20
print(math.perm(5, 2))           # 20 (built-in)
```

---

## Combinations

**Definition:** Selection of n objects without regard to order

$$C(n, r) = \frac{n!}{r!(n-r)!}$$

```python
def combinations(n, r):
    """
    Calculate C(n, r) = n! / (r!(n-r)!)
    Time: O(r)
    Space: O(1)
    """
    if r > n or r < 0:
        return 0
    
    if r == 0 or r == n:
        return 1
    
    r = min(r, n - r)  # Optimization: C(n,r) = C(n,n-r)
    
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    
    return result

# Example: C(5, 2) = ways to choose 2 from 5
# 5 × 4 / (2 × 1) = 10
print(combinations(5, 2))        # 10
print(math.comb(5, 2))           # 10 (built-in)
```

---

# NUMBER THEORY

## Fibonacci Numbers

```python
def fibonacci(n):
    """
    nth Fibonacci number
    Time: O(n)
    Space: O(1)
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

# Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
for i in range(10):
    print(fibonacci(i), end=' ')
# Output: 0 1 1 2 3 5 8 13 21 34
```

---

## Sum Formulas

```python
# Sum of first n natural numbers: n(n+1)/2
def sum_first_n(n):
    return n * (n + 1) // 2

print(sum_first_n(10))  # 55

# Sum of squares: n(n+1)(2n+1)/6
def sum_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

print(sum_squares(10))  # 385

# Sum of cubes: [n(n+1)/2]²
def sum_cubes(n):
    return (n * (n + 1) // 2) ** 2

print(sum_cubes(10))    # 3025
```

---

# WORKED EXAMPLES

## Example 1: Find All Primes Using Sieve

```python
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]

# Find all primes up to 100
primes = sieve_of_eratosthenes(100)
print(primes[:10])  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## Example 2: Modular Exponentiation

```python
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    
    return result

# Calculate 2^100 mod 1000 without overflow
print(mod_exp(2, 100, 1000))  # 376
```

---

# INTERVIEW PREPARATION

## Math Interview Questions

**Q1: How do you check if a number is prime?**
```
A: Check divisibility up to √n only
   Time: O(√n)
   
   if n < 2: return False
   for i in range(2, √n+1):
       if n % i == 0: return False
   return True
```

**Q2: What's modular exponentiation used for?**
```
A: Calculate a^b mod m without overflow
   
   Applications:
   - Cryptography (RSA)
   - Checking large number properties
   - Avoid integer overflow
```

**Q3: Explain sieve of Eratosthenes**
```
A: Find all primes up to n efficiently
   
   Idea: Mark multiples of each prime as composite
   Time: O(n log log n)
   Space: O(n)
```

---

**Master math and bit manipulation. They're 20% of DSA problems.** 🎯

