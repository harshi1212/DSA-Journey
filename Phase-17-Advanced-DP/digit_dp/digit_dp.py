"""
Digit DP
Counting problems with number constraints
"""

def countDigitOne(n):
    """
    Count how many times digit '1' appears in 0 to n.
    
    Key idea: For each digit position, count how many numbers
    have '1' at that position.
    """
    count = 0
    factor = 1  # Current digit position (1, 10, 100, ...)
    
    while factor <= n:
        # Split number into higher and lower parts
        higher = n // (factor * 10)
        cur = (n // factor) % 10
        lower = n % factor
        
        if cur == 0:
            # '1' can only come from higher part
            count += higher * factor
        elif cur == 1:
            # '1' from higher part + partial lower part
            count += higher * factor + lower + 1
        else:  # cur > 1
            # '1' definitely appears in this position
            count += (higher + 1) * factor
        
        factor *= 10
    
    return count

def countByDigits(n):
    """
    Count numbers with specific digit patterns up to n.
    Using digit DP with memoization.
    """
    s = str(n)
    memo = {}
    
    def dp(pos, tight, started):
        """
        pos: current position in number
        tight: whether we're still bounded by n
        started: whether we've started placing non-zero digits
        """
        if pos == len(s):
            return 1 if started else 0
        
        state = (pos, tight, started)
        if state in memo:
            return memo[state]
        
        limit = int(s[pos]) if tight else 9
        result = 0
        
        for digit in range(0, limit + 1):
            new_tight = tight and (digit == limit)
            new_started = started or (digit != 0)
            result += dp(pos + 1, new_tight, new_started)
        
        memo[state] = result
        return result
    
    return dp(0, True, False)

def countNumbersWithDigit1(n):
    """Count numbers from 1 to n containing digit 1."""
    s = str(n)
    memo = {}
    
    def dp(pos, tight, has_one):
        """
        has_one: whether we've placed a '1'
        """
        if pos == len(s):
            return 1 if has_one else 0
        
        state = (pos, tight, has_one)
        if state in memo:
            return memo[state]
        
        limit = int(s[pos]) if tight else 9
        result = 0
        
        for digit in range(0, limit + 1):
            new_tight = tight and (digit == limit)
            new_has_one = has_one or (digit == 1)
            result += dp(pos + 1, new_tight, new_has_one)
        
        memo[state] = result
        return result
    
    return dp(0, True, False)

# Example 1: Count digit 1
print("=== Digit DP: Count Digit One ===\n")

test_numbers = [13, 824, 9999]

for n in test_numbers:
    count = countDigitOne(n)
    print(f"Digit '1' appears in 0-{n}: {count} times")

print("\nExplanation for n=13:")
print("Numbers with 1: 1, 10, 11, 12, 13")
print("Count of 1s: 1 (in 1) + 1 (in 10) + 2 (in 11) + 1 (in 12) + 1 (in 13) = 6")

# Example 2: Count by digit DP
print("\n=== Digit DP: General Counting ===\n")

for n in [10, 100, 1000]:
    count = countByDigits(n)
    print(f"Numbers from 0-{n}: {count}")

# Example 3: Numbers containing digit 1
print("\n=== Numbers Containing Digit 1 ===\n")

for n in [13, 100, 200]:
    count = countNumbersWithDigit1(n)
    print(f"Numbers 1-{n} with digit '1': {count}")

print("\nVerify for n=13:")
nums_with_1 = [i for i in range(1, 14) if '1' in str(i)]
print(f"Manual count: {nums_with_1} = {len(nums_with_1)} numbers")

# Example 4: Pattern explanation
print("\n=== Digit DP Intuition ===")
print("""
For n = 13:
- Ones digit: appears in 1, 11 = 2 times
- Tens digit: appears in 10, 11, 12, 13 = 4 times
- Total: 6

Digit DP approach:
- For each position (ones, tens, hundreds, ...)
- Count how many numbers have '1' at that position
- Respecting upper bound n
- Consider if we're "tight" (still bounded) or free
""")

print("\n=== Digit DP Complexity ===")
print("States: O(len(n) * 2 * 2) = O(log n)")
print("Digits: 0-9 = O(10)")
print("Total: O(10 * log n) - linear in number of digits!")
print("\nUse when: Counting problems with digit/range constraints")
