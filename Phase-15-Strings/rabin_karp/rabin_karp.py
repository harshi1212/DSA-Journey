"""
Rabin-Karp Algorithm
Hashing-based pattern matching, great for multiple patterns
"""

def rabin_karp_search(text, pattern, prime=101):
    """
    Find all occurrences using hashing.
    Useful when: multiple patterns, 2D patterns
    """
    n = len(text)
    m = len(pattern)
    
    if m > n:
        return []
    
    hash_pattern = 0
    hash_text = 0
    power = 1
    base = 256  # Character set size
    
    # Calculate (base^(m-1)) % prime
    for i in range(m - 1):
        power = (power * base) % prime
    
    # Calculate hash of pattern and first window
    for i in range(m):
        hash_pattern = (base * hash_pattern + ord(pattern[i])) % prime
        hash_text = (base * hash_text + ord(text[i])) % prime
    
    matches = []
    
    # Slide window
    for i in range(n - m + 1):
        # Hash matches
        if hash_pattern == hash_text:
            # Verify (avoid false positives)
            if text[i:i+m] == pattern:
                matches.append(i)
        
        # Calculate hash of next window
        if i < n - m:
            hash_text = (base * (hash_text - ord(text[i]) * power) + ord(text[i+m])) % prime
            if hash_text < 0:
                hash_text += prime
    
    return matches

# Example 1: Basic usage
print("=== Rabin-Karp Algorithm ===\n")

text = "ABCCDDAEFFGDAA"
pattern = "AAD"

print(f"Text:    {text}")
print(f"Pattern: {pattern}\n")

matches = rabin_karp_search(text, pattern)
print(f"Matches at: {matches}")

# Example 2: Multiple patterns (main advantage of Rabin-Karp)
print("\n=== Multiple Patterns (Rabin-Karp Advantage) ===\n")

text = "The quick brown fox jumps over the lazy dog"
patterns = ["fox", "the", "lazy", "dog"]

print(f"Text: {text}\n")
print("Finding multiple patterns:")

for pattern in patterns:
    matches = rabin_karp_search(text.lower(), pattern.lower())
    print(f"  '{pattern}': {matches}")

# Example 3: 2D pattern matching (simplified)
print("\n=== 2D Pattern Matching ===\n")

def rabin_karp_2d(grid, pattern):
    """Find pattern in 2D grid."""
    rows = len(grid)
    cols = len(grid[0])
    
    p_rows = len(pattern)
    p_cols = len(pattern[0])
    
    matches = []
    
    # For each possible position
    for i in range(rows - p_rows + 1):
        for j in range(cols - p_cols + 1):
            # Check if pattern matches
            match = True
            for pi in range(p_rows):
                for pj in range(p_cols):
                    if grid[i+pi][j+pj] != pattern[pi][pj]:
                        match = False
                        break
                if not match:
                    break
            
            if match:
                matches.append((i, j))
    
    return matches

grid = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
]

pattern = [
    ['b', 'c'],
    ['e', 'f'],
]

print("Grid:")
for row in grid:
    print("  " + " ".join(row))

print("\nPattern:")
for row in pattern:
    print("  " + " ".join(row))

matches = rabin_karp_2d(grid, pattern)
print(f"\nMatches at: {matches}")

# Example 4: Compare algorithms
print("\n=== Comparison: KMP vs Rabin-Karp ===\n")

comparison = """
                KMP             Rabin-Karp
────────────────────────────────────────────────
Single pattern  Best            Good
Multiple        OK              BEST ✓
2D patterns     Hard            Good ✓
Average time    O(n+m)          O(n+m)
Worst time      O(n+m)          O(nm) [hash collisions]
Space           O(m)            O(1)

When to use:
- KMP: Single pattern, need guaranteed O(n+m)
- Rabin-Karp: Multiple patterns, 2D patterns, plagiarism detection
"""

print(comparison)

print("\n=== Complexity ===")
print("Build hash: O(m)")
print("Search:     O((n-m+1) * m) avg = O(n+m)")
print("Worst:      O(nm) if many hash collisions")
print("Space:      O(1)")
