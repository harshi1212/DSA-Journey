"""
TOPIC: Prime Numbers
Difficulty: Beginner

A prime number is only divisible by 1 and itself.
Why: Used in hashing, cryptography, and many algorithms.
Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23...
"""

print("=== PRIME NUMBERS ===\n")

# Check if a number is prime (Naive approach)
# Why: Simplest way, but slower for large numbers
def is_prime_naive(n):
    # Edge cases
    if n < 2:
        return False
    
    # Check if any number divides n
    for i in range(2, n):
        if n % i == 0:  # If divisible
            return False  # Not prime
    
    return True

# Test it
print("Naive approach:")
test_numbers = [2, 3, 4, 5, 10, 11, 20, 23]
for num in test_numbers:
    print(f"{num}: {is_prime_naive(num)}", end=" | ")
print()

# Better approach: Check only up to sqrt(n)
# Why: If n = a*b, one of a or b must be ≤ sqrt(n)
def is_prime(n):
    if n < 2:
        return False
    
    if n == 2:  # 2 is prime
        return True
    
    if n % 2 == 0:  # Even numbers (except 2) aren't prime
        return False
    
    # Check odd numbers from 3 to sqrt(n)
    # Why: No need to check beyond sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

# Test it
print("Optimized approach:")
for num in test_numbers:
    print(f"{num}: {is_prime(num)}", end=" | ")
print()

# Find all primes up to n (Sieve of Eratosthenes)
# Why: Fast way to find many primes at once
def sieve_of_eratosthenes(n):
    # Create a list assuming all are prime
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False  # 0 and 1 aren't prime
    
    # Mark multiples of each prime as not prime
    for i in range(2, int(n**0.5) + 1):
        if is_prime_arr[i]:
            # Mark all multiples of i as not prime
            for j in range(i*i, n + 1, i):
                is_prime_arr[j] = False
    
    # Collect all primes
    return [i for i in range(n + 1) if is_prime_arr[i]]

# Test it
print("\nSieve approach (find all primes up to 30):")
primes = sieve_of_eratosthenes(30)
print(f"Primes: {primes}")

# Count primes up to n
# Why: Useful for analysis
print(f"\nNumber of primes up to 100: {len(sieve_of_eratosthenes(100))}")

# Find prime factors
# Why: Break number into prime components
def prime_factors(n):
    factors = []
    
    # Check for 2s
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is still > 1, it's prime
    if n > 1:
        factors.append(n)
    
    return factors

# Test it
print("\nPrime Factorization:")
test_nums = [12, 30, 100, 97]
for num in test_nums:
    factors = prime_factors(num)
    print(f"{num} = {' × '.join(map(str, factors))}")
