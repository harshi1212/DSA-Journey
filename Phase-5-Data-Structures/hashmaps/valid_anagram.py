"""
Problem: Valid Anagram
Platform: LeetCode #242
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

My thought process:
  Step 1 — Input and output: Two strings s and t.
           Check if t is an anagram of s (same letters, different order).
  Step 2 — Brute force: Sort both strings and compare.
  Step 3 — Why brute force is slow: O(n log n) due to sorting.
  Step 4 — Optimised approach: Count letter frequencies using hash map.
           If frequencies match, it's an anagram.
  Step 5 — Edge cases: Different lengths? Empty strings?

Approach: Count character frequencies in both strings, compare
Time complexity:  O(n) — one pass to count, one pass to compare
Space complexity: O(1) — at most 26 letters in alphabet (constant)
"""

def isAnagram(s, t):
    """
    Check if t is an anagram of s.
    Anagram: same letters in different order.
    """
    # If different lengths, can't be anagrams
    if len(s) != len(t):
        return False
    
    # Count frequency of each character in s
    # Why: Hash map for O(1) lookup and counting
    char_count = {}
    
    for char in s:
        # If we've seen this char before, increment count
        # Otherwise, set count to 1
        char_count[char] = char_count.get(char, 0) + 1
    
    # Check if t has same character frequencies
    for char in t:
        # If character not in count, t has extra character
        if char not in char_count:
            return False
        
        # Decrease count (we found one occurrence)
        char_count[char] -= 1
        
        # If count goes negative, t has more of this char than s
        if char_count[char] < 0:
            return False
    
    return True

# Alternatively: Use Python's Counter
from collections import Counter

def isAnagramCounter(s, t):
    """Alternative solution using Counter."""
    return Counter(s) == Counter(t)

# ── Test cases ────────────────────────────
print("Test 1:")
s = "anagram"
t = "nagaram"
print(f"Input: s='{s}', t='{t}'")
print(f"Output: {isAnagram(s, t)}")  # Expected: True

print("\nTest 2:")
s = "rat"
t = "car"
print(f"Input: s='{s}', t='{t}'")
print(f"Output: {isAnagram(s, t)}")  # Expected: False

print("\nTest 3:")
s = "abc"
t = "acb"
print(f"Input: s='{s}', t='{t}'")
print(f"Output: {isAnagram(s, t)}")  # Expected: True

print("\nTest 4 (Edge case):")
s = "a"
t = "b"
print(f"Input: s='{s}', t='{t}'")
print(f"Output: {isAnagram(s, t)}")  # Expected: False
