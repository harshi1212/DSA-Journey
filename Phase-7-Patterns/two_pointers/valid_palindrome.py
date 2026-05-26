"""
Pattern: Two Pointers
Difficulty: Medium

Use two pointers from opposite ends.
Why: Meet in middle, compare pairs efficiently.
"""

# Example 1: Valid Palindrome (with two pointers)
def isPalindrome(s):
    """Check if string is palindrome using two pointers."""
    # Clean: keep only alphanumeric, lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    left = 0
    right = len(cleaned) - 1
    
    # Move towards middle
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

print("Two Pointers - Palindrome:")
print(f"'A man, a plan, a canal: Panama': {isPalindrome('A man, a plan, a canal: Panama')}")  # True
print(f"'race a car': {isPalindrome('race a car')}")  # False

# Example 2: Two Sum (sorted array)
def twoSum(arr, target):
    """Find two numbers that sum to target in sorted array."""
    left = 0
    right = len(arr) - 1
    
    while left < right:
        total = arr[left] + arr[right]
        
        if total == target:
            return [arr[left], arr[right]]
        elif total < target:
            left += 1
        else:
            right -= 1
    
    return None

print("\nTwo Pointers - Two Sum:")
arr = [1, 3, 5, 7, 9]
print(f"Array {arr}, target 12: {twoSum(arr, 12)}")  # [3, 9] or [5, 7]

# Example 3: Reverse String (in-place)
def reverseString(s):
    """Reverse string using two pointers."""
    s = list(s)  # Convert to list (mutable)
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)

print("\nTwo Pointers - Reverse String:")
print(f"Reverse 'hello': {reverseString('hello')}")  # 'olleh'
