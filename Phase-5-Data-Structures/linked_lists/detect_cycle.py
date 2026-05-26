"""
Problem: Detect Cycle in Linked List
Platform: LeetCode #141
Difficulty: Easy
Link: https://leetcode.com/problems/linked-list-cycle/

My thought process:
  Step 1 — Input and output: Head of linked list.
           Detect if there's a cycle (node points back to earlier node).
  Step 2 — Brute force: Store all visited nodes in a set.
  Step 3 — Why brute force is slow: Uses O(n) extra space.
  Step 4 — Optimised approach: Floyd's cycle detection (tortoise and hare).
           Fast pointer moves 2 steps, slow pointer moves 1 step.
           If they meet, there's a cycle.
  Step 5 — Edge cases: Empty list? Single node? No cycle?

Approach: Two pointers moving at different speeds
Time complexity:  O(n) — visits each node
Space complexity: O(1) — only two pointers
"""

class ListNode:
    """Node in a linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    """
    Detect if linked list has a cycle.
    Uses Floyd's Cycle Detection Algorithm (tortoise and hare).
    """
    # Edge case
    if not head or not head.next:
        return False
    
    # Two pointers at different speeds
    slow = head          # Moves 1 step
    fast = head          # Moves 2 steps
    
    # Keep moving until we find a cycle or reach end
    while fast and fast.next:
        # Move slow one step
        slow = slow.next
        
        # Move fast two steps
        fast = fast.next.next
        
        # If they meet, there's a cycle
        # Why: If there's a cycle, fast will eventually catch slow
        if slow == fast:
            return True
    
    # Reached end without meeting, no cycle
    return False

# ── Test cases ────────────────────────────

print("Test 1 (No cycle):")
# Create: 1→2→3→4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(f"Has cycle: {hasCycle(head)}")  # Expected: False

print("\nTest 2 (Has cycle):")
# Create: 1→2→3→4→(back to 2)
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Creates cycle back to node2
print(f"Has cycle: {hasCycle(node1)}")  # Expected: True

print("\nTest 3 (Self cycle):")
# Create: 1→(back to 1)
node = ListNode(1)
node.next = node  # Points to itself
print(f"Has cycle: {hasCycle(node)}")  # Expected: True

print("\nTest 4 (Edge case):")
# Single node, no cycle
head = ListNode(1)
print(f"Has cycle: {hasCycle(head)}")  # Expected: False
