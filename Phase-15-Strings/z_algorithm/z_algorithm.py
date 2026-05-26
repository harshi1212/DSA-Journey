"""
Z-Algorithm
Linear time pattern matching with prefix information
"""

def z_algorithm(s):
    """
    Build Z-array where Z[i] = length of longest substring
    starting from s[i] which is also a prefix of s.
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    
    l, r = 0, 0  # [l, r] is the window
    
    for i in range(1, n):
        if i > r:
            # Outside current window, compute from scratch
            l, r = i, i
            while r < n and s[r - l] == s[r]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            # Inside window, use previously computed value
            k = i - l
            
            if z[k] < r - i + 1:
                # Copied Z value is within bounds
                z[i] = z[k]
            else:
                # Need to extend beyond right boundary
                l = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    
    return z

def z_algorithm_search(text, pattern):
    """Find all occurrences of pattern in text using Z-algorithm."""
    combined = pattern + "$" + text
    z = z_algorithm(combined)
    
    pattern_len = len(pattern)
    matches = []
    
    for i in range(pattern_len + 1, len(combined)):
        if z[i] == pattern_len:
            matches.append(i - pattern_len - 1)
    
    return matches

# Example 1: Basic Z-array
print("=== Z-Algorithm ===\n")

s = "aabaaab"
z = z_algorithm(s)

print(f"String: {s}")
print(f"Index:  {' '.join(str(i) for i in range(len(s)))}")
print(f"Z-arr:  {' '.join(str(z_val) for z_val in z)}")
print()

print("Interpretation:")
for i, z_val in enumerate(z):
    if z_val > 0:
        print(f"  Z[{i}] = {z_val}: '{s[i:i+z_val]}' matches prefix")

# Example 2: Pattern matching
print("\n=== Pattern Matching with Z-Algorithm ===\n")

text = "ABCCDDAEFGDAAAZ"
pattern = "AAA"

print(f"Text:    {text}")
print(f"Pattern: {pattern}\n")

matches = z_algorithm_search(text, pattern)
print(f"Matches at: {matches}")

combined = pattern + "$" + text
z_combined = z_algorithm(combined)
print(f"\nCombined: {combined}")
print(f"Z-array:  {z_combined}")

# Example 3: Periodic string detection
print("\n=== Detect Period ===\n")

def find_period(s):
    """Find period of string using Z-algorithm."""
    z = z_algorithm(s)
    n = len(s)
    
    for period in range(1, n):
        if n % period == 0:
            # Check if this period works
            if z[period] == n - period:
                return period
    
    return n

strings = ["abcabc", "aaaa", "abcdefgh", "abab", "ababab"]

print("Period detection:")
for s in strings:
    period = find_period(s)
    print(f"  '{s}': period = {period} ('{s[:period]}')")

# Example 4: Count occurrences
print("\n=== Count Occurrences ===\n")

def count_pattern_occurrences(text, pattern):
    """Count how many times pattern appears in text."""
    matches = z_algorithm_search(text, pattern)
    return len(matches)

test_cases = [
    ("mississippi", "issi"),
    ("aaaa", "aa"),
    ("abcabcabc", "abc"),
]

for text, pattern in test_cases:
    count = count_pattern_occurrences(text, pattern)
    matches = z_algorithm_search(text, pattern)
    print(f"'{pattern}' in '{text}': {count} times at {matches}")

print("\n=== Complexity ===")
print("Build Z-array: O(n)")
print("Search:        O(n + m)")
print("Total:         O(n + m) - linear!")
print("Space:         O(n)")
print("\nAdvantage: Z-array gives prefix info, useful for many problems")
