"""
KMP (Knuth-Morris-Pratt) Algorithm
Pattern matching in O(n+m) time
"""

def build_lps(pattern):
    """
    Build Longest Proper Prefix-Suffix array.
    LPS[i] = length of longest prefix of pattern[0:i+1]
             that is also a suffix of pattern[0:i+1]
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Find all occurrences of pattern in text using KMP.
    Returns list of starting indices.
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return []
    
    lps = build_lps(pattern)
    matches = []
    
    i = 0  # Index in text
    j = 0  # Index in pattern
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        if j == m:
            # Found match at position i - j
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            # Mismatch
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

# Example 1: Basic pattern matching
print("=== KMP Algorithm ===\n")

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"

print(f"Text:    {text}")
print(f"Pattern: {pattern}\n")

lps = build_lps(pattern)
print(f"LPS array: {lps}")
print(f"Interpretation:")
print(f"  LPS[8] = {lps[8]}: Last 8 chars have '{pattern[:lps[8]]}' as prefix-suffix\n")

matches = kmp_search(text, pattern)
print(f"Matches found at indices: {matches}")
if matches:
    for idx in matches:
        print(f"  {' ' * idx}{pattern}")

# Example 2: Multiple occurrences
print("\n=== Find All Occurrences ===\n")

text = "aabaab"
pattern = "aab"

print(f"Text:    {text}")
print(f"Pattern: {pattern}\n")

matches = kmp_search(text, pattern)
print(f"Occurrences at: {matches}")

for idx in matches:
    print(f"Position {idx}: {text[idx:idx+len(pattern)]}")

# Example 3: LPS array building process
print("\n=== LPS Array Building ===\n")

patterns = ["ABABAC", "ABCAB", "AABAAAB"]

for pat in patterns:
    lps = build_lps(pat)
    print(f"Pattern: {pat}")
    print(f"Index:   {' '.join(str(i) for i in range(len(pat)))}")
    print(f"LPS:     {' '.join(str(l) for l in lps)}")
    print()

# Example 4: Compare with naive
print("=== KMP vs Naive (Performance) ===\n")

import time

# Worst case for naive: pattern at end
text_large = "A" * 10000 + "AAAB"
pattern_hard = "AAAB"

# KMP
start = time.time()
matches_kmp = kmp_search(text_large, pattern_hard)
time_kmp = time.time() - start

# Naive
def naive_search(text, pattern):
    matches = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            matches.append(i)
    return matches

start = time.time()
matches_naive = naive_search(text_large, pattern_hard)
time_naive = time.time() - start

print(f"Text length: {len(text_large)}, Pattern length: {len(pattern_hard)}")
print(f"KMP time:   {time_kmp*1000:.3f}ms")
print(f"Naive time: {time_naive*1000:.3f}ms")
print(f"KMP is {time_naive/time_kmp:.1f}x faster")

# Example 5: implement strStr() using KMP
print("\n=== Implement strStr() ===\n")

def strStr(haystack, needle):
    """Find first occurrence of needle in haystack."""
    matches = kmp_search(haystack, needle)
    return matches[0] if matches else -1

test_cases = [
    ("hello", "ll"),
    ("aaaa", "bba"),
    ("", ""),
    ("a", "a"),
    ("mississippi", "issip"),
]

for haystack, needle in test_cases:
    result = strStr(haystack, needle)
    print(f"'{haystack}' contains '{needle}': {result}")

print("\n=== Complexity ===")
print("Build LPS:  O(m) - m = pattern length")
print("Search:     O(n) - n = text length")
print("Total:      O(n + m) - linear!")
print("Space:      O(m) - for LPS array")
