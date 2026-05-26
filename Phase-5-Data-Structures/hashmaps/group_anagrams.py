"""
Problem: Group Anagrams
Platform: LeetCode #49
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

My thought process:
  Step 1 — Input and output: List of strings.
           Return list of lists, where each list contains anagrams.
  Step 2 — Brute force: Compare every string with every other string.
  Step 3 — Why brute force is slow: O(n²) - compare all pairs.
  Step 4 — Optimised approach: Sort characters in each word as key.
           Anagrams have same sorted characters.
           Use hash map: sorted_word → list of anagrams.
  Step 5 — Edge cases: Empty list? Single character strings?

Approach: Use sorted characters as key in hash map
Time complexity:  O(n*k log k) where n=number of words, k=avg word length
Space complexity: O(n*k) — store all characters in hash map
"""

def groupAnagrams(strs):
    """
    Group strings that are anagrams together.
    Return list of lists, each containing anagrams.
    """
    # Hash map: sorted_word → list of anagrams
    # Why: Anagrams have same sorted form
    anagram_map = {}
    
    for word in strs:
        # Key: sorted characters of the word
        # Why: "listen" and "silent" both sort to "eilnst"
        key = ''.join(sorted(word))
        
        # If this key doesn't exist yet, create empty list
        if key not in anagram_map:
            anagram_map[key] = []
        
        # Add word to its anagram group
        anagram_map[key].append(word)
    
    # Return all anagram groups as a list
    return list(anagram_map.values())

# Alternative approach: Use character count as key
def groupAnagramsCounter(strs):
    """Alternative using character frequency as key."""
    from collections import Counter, defaultdict
    
    # Use tuple of sorted character counts as key
    # Why: More efficient than string sorting
    anagram_map = defaultdict(list)
    
    for word in strs:
        # Create key from sorted characters
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    
    return list(anagram_map.values())

# ── Test cases ────────────────────────────
print("Test 1:")
strs = ["eat", "tea", "ate", "eat", "tan", "ate", "nat"]
print(f"Input: {strs}")
result = groupAnagrams(strs)
print(f"Output: {result}")
# Expected: [["eat","tea","ate"], ["tan","nat"]] (order may vary)

print("\nTest 2:")
strs = ["a"]
print(f"Input: {strs}")
result = groupAnagrams(strs)
print(f"Output: {result}")  # Expected: [["a"]]

print("\nTest 3:")
strs = [""]
print(f"Input: {strs}")
result = groupAnagrams(strs)
print(f"Output: {result}")  # Expected: [[""]]

print("\nTest 4:")
strs = ["listen", "silent", "hello", "world"]
print(f"Input: {strs}")
result = groupAnagrams(strs)
print(f"Output: {result}")
# Expected: [["listen","silent"], ["hello"], ["world"]] (order may vary)
