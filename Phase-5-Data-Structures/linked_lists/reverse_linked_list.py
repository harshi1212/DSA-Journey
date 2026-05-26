"""
Problem: Reverse Linked List
Platform: LeetCode #206
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/

My thought process:
  Step 1 — Input and output: Head of linked list.
           Reverse the links: A→B→C becomes C→B→A.
  Step 2 — Brute force: Recursion or complex logic.
  Step 3 — Why brute force is slow: Harder to understand, easy to mess up.
  Step 4 — Optimised approach: Three pointers (prev, curr, next).
           Reverse link one at a time.
  Step 5 — Edge cases: Empty list? Single node?

Approach: Iterative with three pointers
Time complexity:  O(n) — visit each node once
Space complexity: O(1) — only a few pointers
"""

class ListNode:
    """Node in a linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    Reverse a linked list.
    A→B→C becomes C→B→A.
    """
    # Three pointers to track previous, current, next
    prev = None
    curr = head
    
    # Traverse and reverse each link
    while curr:
        # Store next node before we lose the reference
        # Why: We're about to change curr.next
        next_temp = curr.next
        
        # Reverse the link: point to previous instead of next
        # Why: This is the reversal step
        curr.next = prev
        
        # Move forward: prev becomes curr
        prev = curr
        # And curr becomes next node
        curr = next_temp
    
    # prev is now the new head (old tail)
    return prev

# ── Test cases ────────────────────────────

def list_to_array(head):
    """Convert linked list to array for easy printing."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

print("Test 1:")
# Create: 1→2→3→4→5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(f"Original: {list_to_array(head)}")
head = reverseList(head)
print(f"Reversed: {list_to_array(head)}")  # Expected: [5,4,3,2,1]

print("\nTest 2:")
# Create: 1→2
head = ListNode(1, ListNode(2))
print(f"Original: {list_to_array(head)}")
head = reverseList(head)
print(f"Reversed: {list_to_array(head)}")  # Expected: [2,1]

print("\nTest 3 (Edge case):")
# Single node
head = ListNode(1)
print(f"Original: {list_to_array(head)}")
head = reverseList(head)
print(f"Reversed: {list_to_array(head)}")  # Expected: [1]
