# Fast and Slow Pointers

## What is it?
Two pointers moving through a linked list 
at different speeds.
Fast pointer moves 2 steps at a time.
Slow pointer moves 1 step at a time.

Think of it like two runners on a circular 
track — the faster one will eventually lap 
the slower one if there is a loop.

## Why it works for cycle detection
If there is NO cycle: fast pointer reaches 
the end (None) first.
If there IS a cycle: fast pointer keeps 
going in circles and eventually meets 
the slow pointer.

## The template
slow = head
fast = head
while fast and fast.next:
    slow = slow.next        # 1 step
    fast = fast.next.next   # 2 steps
    if slow == fast:
        return True  # cycle found

## Other uses
Finding the middle of a linked list:
When fast reaches the end, slow is at 
the middle.

## Common mistake
Checking fast == slow before moving them.
Always move first, then check.

## Practice problems
- Easy: Linked List Cycle (LeetCode #141)
- Medium: Find Duplicate Number (LeetCode #287)
- Hard: Reorder List (LeetCode #143)
