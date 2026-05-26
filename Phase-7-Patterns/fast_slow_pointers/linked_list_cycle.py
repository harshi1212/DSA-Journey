# Fast & Slow Pointers Pattern

print("=== FAST & SLOW POINTERS PATTERN ===\n")

print("""
TECHNIQUE: Two pointers at different speeds
- Slow pointer: moves 1 step
- Fast pointer: moves 2 steps
- If they meet → cycle exists

WHY:
In a cycle, fast pointer will eventually catch slow pointer.
Guarantees O(1) space for cycle detection.

USE CASES:
1. Detect cycle in linked list
2. Find cycle start position
3. Find middle of linked list
4. Remove duplicate from sorted list
""")

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Example: Find middle of linked list
def findMiddle(head):
    """Find middle node of linked list."""
    slow = head
    fast = head
    
    # Fast moves 2, slow moves 1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Test
print("Example: Find Middle of Linked List")
# Create: 1 → 2 → 3 → 4 → 5
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

middle = findMiddle(node1)
print(f"Middle value: {middle.val}")  # 3

# Example: Cycle detection (from earlier)
def hasCycle(head):
    """Detect cycle using fast/slow pointers."""
    if not head:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

print("\nExample: Detect Cycle")
# Create cycle: 1 → 2 → 3 → 4 → 2
cycleNode = Node(2)
cycleNode.next = Node(3)
cycleNode.next.next = Node(4)
cycleNode.next.next.next = cycleNode  # Creates cycle back to 2

head = Node(1)
head.next = cycleNode

print(f"Has cycle: {hasCycle(head)}")  # True
