# Sliding Window Pattern

print("=== SLIDING WINDOW PATTERN ===\n")

# Example 1: Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    """
    Find length of longest substring without repeating characters.
    Window: characters currently in substring
    """
    # Set of characters in current window
    seen = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Remove leftmost characters until no duplicates
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        # Add current character to window
        seen.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

print("Longest Substring Without Repeating:")
print(f"'abcabcbb': {lengthOfLongestSubstring('abcabcbb')}")  # 3 ('abc')
print(f"'bbbbb': {lengthOfLongestSubstring('bbbbb')}")        # 1 ('b')
print(f"'pwwkew': {lengthOfLongestSubstring('pwwkew')}")      # 3 ('wke')

# Example 2: Maximum Average Subarray
def findMaxAverage(nums, k):
    """
    Find maximum average of subarray of length k.
    Fixed-size window.
    """
    # Calculate initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    # Slide window: remove left, add right
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum / k

print("\nMaximum Average Subarray (k=4):")
nums = [1, 12, -5, -6, 50, 3]
print(f"nums={nums}: {findMaxAverage(nums, 4):.2f}")  # 12.75 ([12, -5, -6, 50])

# Example 3: Contains Duplicate II
def containsNearbyDuplicate(nums, k):
    """
    Check if array contains duplicates at most k positions apart.
    Sliding window of size k.
    """
    window = set()
    
    for i in range(len(nums)):
        # If duplicate found in window, return True
        if nums[i] in window:
            return True
        
        # Add to window
        window.add(nums[i])
        
        # Keep window size <= k
        if len(window) > k:
            window.remove(nums[i - k])
    
    return False

print("\nContains Duplicate II (k=2):")
print(f"[99,99] k=2: {containsNearbyDuplicate([99, 99], 2)}")  # True
print(f"[1,2,3,1] k=3: {containsNearbyDuplicate([1, 2, 3, 1], 3)}")  # True
print(f"[1,2,3,1] k=2: {containsNearbyDuplicate([1, 2, 3, 1], 2)}")  # False
