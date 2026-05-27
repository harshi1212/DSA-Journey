# Phase 5 - Data Structures (Complete Master Guide)

**Foundation of all DSA. Master these data structures completely.**

---

## Table of Contents
1. [Formal Definitions](#formal-definitions)
2. [Data Structure Fundamentals](#data-structure-fundamentals)
3. [Arrays & Strings](#arrays--strings)
4. [Hash Maps & Sets](#hash-maps--sets)
5. [Stacks & Queues](#stacks--queues)
6. [Linked Lists](#linked-lists)
7. [Trees & Binary Search Trees](#trees--binary-search-trees)
8. [Heaps & Priority Queues](#heaps--priority-queues)
9. [Graph Representation](#graph-representation)
10. [Complexity Comparison](#complexity-comparison)
11. [Choosing Data Structures](#choosing-data-structures)
12. [Worked Examples (50+)](#worked-examples)
13. [Interview Preparation](#interview-preparation)

---

# FORMAL DEFINITIONS

## What is a Data Structure?

**Definition:** A data structure is a systematic way to organize and store data in computer memory to enable efficient access, modification, and analysis operations.

**Components:**
1. **Organization:** How data is arranged in memory
2. **Operations:** What actions can be performed (CRUD)
3. **Complexity:** Time and space trade-offs

**Mathematical Definition:** A data structure DS is a tuple $(S, O)$ where:
- $S$ = Set of states (valid configurations of data)
- $O$ = Set of operations (functions that transform states)

---

## Classification

```
Data Structures
├─ PRIMITIVE
│  ├─ Integer
│  ├─ Float
│  ├─ Boolean
│  └─ Character
│
├─ LINEAR
│  ├─ Array (contiguous memory)
│  ├─ String (sequence of characters)
│  ├─ Linked List (nodes with pointers)
│  ├─ Stack (LIFO)
│  └─ Queue (FIFO)
│
├─ HIERARCHICAL
│  ├─ Binary Tree
│  ├─ Binary Search Tree
│  ├─ Heap
│  ├─ Trie
│  └─ Segment Tree
│
└─ GRAPH-BASED
   ├─ Graph (adjacency list/matrix)
   ├─ Directed Graph
   ├─ Weighted Graph
   └─ Hash Map/Set
```

---

# DATA STRUCTURE FUNDAMENTALS

## Memory Layout

**How data is stored in computer memory:**

```
Memory addresses: 1000  1001  1002  1003  1004  1005  1006  1007

Array [10, 20, 30]:
├─ 10 stored at address 1000
├─ 20 stored at address 1001
└─ 30 stored at address 1002

Linked List 10→20→30:
├─ 10 with pointer to address 2000 (stored at 1000)
├─ 20 with pointer to address 3000 (stored at 2000)
└─ 30 with pointer to None (stored at 3000)

KEY INSIGHT:
Array: All elements in consecutive memory → O(1) access
Linked List: Elements scattered, connected by pointers → O(n) access
```

## Operations Taxonomy

Every data structure supports these categories:

### 1. Creation/Initialization
```python
# Array
arr = []
arr = [1, 2, 3]

# Linked List
head = Node(1)
head.next = Node(2)
```

### 2. Access/Retrieval
```python
# Array: O(1)
value = arr[0]

# Linked List: O(n)
current = head
while current:
    value = current.data
    current = current.next
```

### 3. Insertion
```python
# Array: O(n) - shift elements
arr.insert(1, 99)

# Linked List: O(1) - if you have pointer
node.next = new_node
new_node.next = node.next.next
```

### 4. Deletion
```python
# Array: O(n) - shift elements back
arr.pop(1)

# Linked List: O(1) - if you have pointer
node.next = node.next.next
```

### 5. Modification
```python
# Array: O(1)
arr[0] = 100

# Linked List: O(1) - if you have pointer
node.data = 100
```

### 6. Searching
```python
# Array: O(n) unsorted, O(log n) binary search
# Linked List: O(n)
# Hash Map: O(1) average
```

---

# ARRAYS & STRINGS

## Arrays - Formal Definition

**Definition:** An array is a fixed-size, contiguous block of memory storing elements of the same type, indexed from 0 to n-1.

**Mathematical Notation:**
```
Array A = [a₀, a₁, a₂, ..., aₙ₋₁]
where each aᵢ is an element
and elements occupy addresses: base_address + i
```

---

## Array Operations with Proofs

### Random Access - O(1)

**Claim:** Accessing arr[i] is O(1)

**Proof:**
```
Base address: b
Element at index i: located at address b + i
Retrieval: Direct memory lookup at address b + i
Time: Constant (doesn't depend on i or n)
Therefore: O(1) ✓
```

### Linear Search - O(n)

**Claim:** Searching unsorted array is O(n)

**Proof:**
```
Worst case: element at end or not present
Must check all n elements: a₀, a₁, ..., aₙ₋₁
Operations: n comparisons
Time: T(n) = n = O(n) ✓
```

### Binary Search - O(log n)

**Claim:** Searching sorted array is O(log n)

**Proof:**
```
Each iteration eliminates half:
n → n/2 → n/4 → n/8 → ... → 1

Number of halvings: log₂(n)
Therefore: O(log n) ✓
```

---

## Array Implementation Details

```python
# Python lists are dynamic arrays
arr = []  # Empty array
arr.append(1)   # O(1) amortized

# Under the hood:
# Python allocates extra space for growth
# When needed, allocates larger block and copies
# Copy operation is O(n) but rare → amortized O(1)

# Growth factor: Python uses ~1.125x growth
capacity = 0
operations = 0
for i in range(1000000):
    arr.append(i)
    if len(arr) == capacity:
        # Reallocation! O(n)
        capacity *= 1.125

# Result: Total O(n) work spread over n operations
# Average per operation: O(1)
```

---

## String Operations

```python
# Strings are immutable character arrays
s = "hello"

# O(1) - Direct access
char = s[0]  # 'h'

# O(n) - Concatenation (creates new string!)
s2 = s + "world"  # New string allocated

# O(n) - Substring
substr = s[1:4]  # Creates new string "ell"

# O(n) - Searching
index = s.find("ll")  # 2

# O(n) - Comparison
if s == "hello":  # Must compare all characters
    pass

# Key insight: String immutability means
# most operations create new strings → O(n) space
```

---

# HASH MAPS & SETS

## Hash Map - Formal Definition

**Definition:** A hash map is a data structure that implements an associative array - a structure that maps keys to values using a hash function.

**Mathematical Definition:**
```
HashMap = (Hash Function h: Keys → Indices,
           Array B: stores key-value pairs)

h(key) = index in array B where value stored
```

---

## How Hash Maps Work (Under the Hood)

```python
# Simple hash map implementation:
class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]  # Buckets for collision
    
    def _hash(self, key):
        """Hash function: maps key to bucket index"""
        return hash(key) % self.size
    
    def set(self, key, value):
        """Store key-value pair"""
        index = self._hash(key)  # Hash the key
        
        # Handle collisions with chaining
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)  # Update
                return
        
        self.buckets[index].append((key, value))  # Insert
    
    def get(self, key):
        """Retrieve value by key"""
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

# Example:
hm = SimpleHashMap(5)
hm.set("apple", 5)
print(hm.get("apple"))  # 5
```

---

## Hash Function Properties

**Good hash function must:**

1. **Deterministic:** Same input always gives same output
```python
h("apple") = 0  # Always 0
h("apple") = 0  # Always 0
```

2. **Uniform Distribution:** Maps keys evenly across range
```python
Keys: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Bad hash: All map to bucket 0 (O(n) lookup!)
Good hash: Evenly distributed across buckets
```

3. **Low Collision Rate:** Different keys map to different buckets
```python
Collision: h("apple") = h("peanut") = same bucket
If no collisions: O(1) lookup
If many collisions: O(n) lookup (search in bucket)
```

---

## Collision Handling

### Method 1: Chaining
```python
# Store lists in each bucket
buckets = [
    [],                    # Bucket 0
    [("apple", 5)],       # Bucket 1
    [("banana", 3), ("orange", 7)],  # Bucket 2 - collision!
    [],
    [("grape", 10)]
]

# Lookup "orange":
index = hash("orange") % 5  # 2
for k, v in buckets[2]:     # Search bucket 2
    if k == "orange":
        return v            # Found!
```

### Method 2: Open Addressing (Linear Probing)
```python
# If hash(key) occupied, try next slot
buckets = ["apple", None, "banana", "orange", None]

# Insert "cherry":
index = hash("cherry") % 5  # 2
while buckets[index] != None:  # Slot occupied
    index = (index + 1) % 5    # Try next slot
buckets[index] = "cherry"
```

---

## Hash Map Complexity

```python
# Average case (good hash, few collisions):
get/set/delete: O(1)

# Worst case (bad hash function, all collisions):
get/set/delete: O(n) [must search through list]

# In practice (Python dict):
# Uses open addressing with good hash
# Complexity: O(1) average, O(n) rare worst case
```

---

## Sets - Unordered Collections

```python
# Set uses hash map internally
s = {1, 2, 3, 4, 5}

# Operations: All O(1) average
s.add(6)          # O(1)
s.remove(3)       # O(1)
2 in s            # O(1)

# Set operations:
s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1 | s2  # {1, 2, 3, 4}  Union - O(n+m)
s1 & s2  # {2, 3}        Intersection - O(min(n,m))
s1 - s2  # {1}           Difference - O(n)
```

---

# STACKS & QUEUES

## Stack - LIFO (Last In First Out)

**Definition:** A stack is a linear data structure where insertion and deletion occur at the same end (top).

**Mathematical Model:**
```
Stack = [bottom, ..., a₂, a₁, a₀]
         where a₀ is top

Push(x):   top ← x, size++
Pop():     x ← top, top ← top-1, size--
Peek():    return top
IsEmpty(): return size == 0
```

**Implementation:**
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):       # O(1)
        self.items.append(item)
    
    def pop(self):              # O(1)
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):             # O(1)
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):         # O(1)
        return len(self.items) == 0

# Usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # 3 (LIFO)
```

**Use Cases:**
- Function call stack (recursion)
- Expression evaluation (infix to postfix)
- Undo/Redo functionality
- Backtracking problems

---

## Queue - FIFO (First In First Out)

**Definition:** A queue is a linear data structure where insertion occurs at rear, deletion at front.

**Mathematical Model:**
```
Queue = [a₀, a₁, a₂, ..., aₙ]
        front                rear

Enqueue(x):  rear ← x, size++
Dequeue():   x ← front, front ← front+1, size--
```

**Implementation:**
```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):    # O(1)
        self.items.append(item)
    
    def dequeue(self):          # O(1)
        if self.is_empty():
            return None
        return self.items.popleft()
    
    def is_empty(self):         # O(1)
        return len(self.items) == 0

# Usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # 1 (FIFO)
```

**Use Cases:**
- BFS (breadth-first search)
- Task scheduling
- Print queue
- Buffering

---

# LINKED LISTS

## Linked List - Formal Definition

**Definition:** A linked list is a linear data structure where each element (node) contains data and a reference (pointer) to the next node.

**Mathematical Definition:**
```
LinkedList = Node₀ → Node₁ → Node₂ → ... → Nodeₙ → None

where each Node = (data, next)
```

**Node Class:**
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create: 1 → 2 → 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
```

---

## Linked List Operations

### Traverse - O(n)
```python
def traverse(head):
    current = head
    while current:
        print(current.data)
        current = current.next

# Proof: O(n)
# - Visit each of n nodes once
# - Each visit: O(1)
# - Total: n × O(1) = O(n)
```

### Search - O(n)
```python
def search(head, target):
    current = head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False

# Proof: O(n)
# Worst case: target at end or not present
# Must check all n nodes
```

### Insert at Beginning - O(1)
```python
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

# Proof: O(1)
# Only manipulate pointers
# Doesn't depend on list length n
```

### Insert at Position - O(n)
```python
def insert_at_position(head, position, data):
    if position == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node
    
    current = head
    for i in range(position - 1):
        if not current.next:
            return head
        current = current.next
    
    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node
    return head

# Proof: O(n)
# Must traverse to position: O(position)
# Worst case: position = n-1
# Therefore: O(n)
```

### Delete - O(n)
```python
def delete_node(head, target):
    if head.data == target:
        return head.next
    
    current = head
    while current.next:
        if current.next.data == target:
            current.next = current.next.next
            return head
        current = current.next
    
    return head

# Proof: O(n)
# Must find node before target: O(n) search
```

---

## Linked List vs Array

| Operation | Array | Linked List |
|-----------|-------|------------|
| Access | O(1) | O(n) |
| Insert (beginning) | O(n) | O(1) |
| Insert (middle) | O(n) | O(n) |
| Delete (beginning) | O(n) | O(1) |
| Delete (middle) | O(n) | O(n) |
| Search | O(n) | O(n) |
| Space | O(n) | O(n) |

**When to use each:**
- **Array:** Fast access needed, few insertions/deletions
- **Linked List:** Frequent insertions/deletions at beginning

---

# TREES & BINARY SEARCH TREES

## Binary Tree - Formal Definition

**Definition:** A binary tree is a tree data structure where each node has at most 2 children (left and right).

**Mathematical Properties:**
```
Height of tree h:        Maximum distance from root to leaf
                        Empty tree: h = -1
                        Single node: h = 0

Node count n:           Number of nodes in tree

For perfect binary tree:
n = 2^(h+1) - 1
```

**Node Class:**
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create tree:
#      1
#     / \
#    2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

---

## Binary Search Tree (BST) - Formal Definition

**Definition:** A binary search tree is a binary tree with the property that for every node:
- All values in left subtree < node value
- All values in right subtree > node value

**Invariant Property:**
```
For all nodes n:
∀ node ∈ left_subtree(n):  node.val < n.val
∀ node ∈ right_subtree(n): node.val > n.val
```

---

## BST Operations

### Search - O(log n) average, O(n) worst

```python
def search_bst(root, target):
    current = root
    while current:
        if current.val == target:
            return True
        elif target < current.val:
            current = current.left
        else:
            current = current.right
    return False

# Analysis:
# Best: target at root = O(1)
# Average: balanced tree = O(log n) [log₂(n) levels]
# Worst: degenerate tree = O(n) [linear chain]
```

### Insert - O(log n) average, O(n) worst

```python
def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    
    return root

# Analysis:
# Best/Average: O(log n) [balanced tree]
# Worst: O(n) [degenerate tree]
```

### Delete - O(log n) average, O(n) worst

```python
def delete_bst(root, val):
    if not root:
        return None
    
    if val < root.val:
        root.left = delete_bst(root.left, val)
    elif val > root.val:
        root.right = delete_bst(root.right, val)
    else:
        # Node found - three cases:
        
        # Case 1: No children (leaf)
        if not root.left and not root.right:
            return None
        
        # Case 2: One child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # Case 3: Two children
        # Find in-order successor (smallest in right subtree)
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete_bst(root.right, successor.val)
    
    return root

def find_min(root):
    while root.left:
        root = root.left
    return root
```

---

# HEAPS & PRIORITY QUEUES

## Heap - Formal Definition

**Definition:** A heap is a complete binary tree that satisfies the heap property:
- **Min Heap:** Parent ≤ children (smallest at root)
- **Max Heap:** Parent ≥ children (largest at root)

**Complete Binary Tree:**
```
Tree is completely filled except possibly last level,
which is filled left to right.

Valid heap (complete):
      1
     / \
    2   3
   / \ /
  4  5 6

Invalid (not complete):
      1
     / \
    2   3
   /     \
  4       6
  (missing 5)
```

---

## Heap Implementation (Array-based)

```python
class MinHeap:
    def __init__(self):
        self.heap = [0]  # Index 0 unused, start at 1
    
    def _parent(self, i):
        return i // 2
    
    def _left_child(self, i):
        return 2 * i
    
    def _right_child(self, i):
        return 2 * i + 1
    
    def push(self, val):           # O(log n)
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)
    
    def pop(self):                 # O(log n)
        if len(self.heap) == 1:
            return None
        
        min_val = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self._bubble_down(1)
        return min_val
    
    def _bubble_up(self, i):
        while i > 1 and self.heap[i] < self.heap[self._parent(i)]:
            # Swap with parent
            self.heap[i], self.heap[self._parent(i)] = \
                self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)
    
    def _bubble_down(self, i):
        while self._left_child(i) < len(self.heap):
            smaller_child = self._left_child(i)
            
            if self._right_child(i) < len(self.heap) and \
               self.heap[self._right_child(i)] < self.heap[smaller_child]:
                smaller_child = self._right_child(i)
            
            if self.heap[i] <= self.heap[smaller_child]:
                break
            
            # Swap with smaller child
            self.heap[i], self.heap[smaller_child] = \
                self.heap[smaller_child], self.heap[i]
            i = smaller_child

# Usage:
heap = MinHeap()
for val in [5, 3, 7, 1]:
    heap.push(val)

while True:
    val = heap.pop()
    if val is None:
        break
    print(val)  # Prints 1, 3, 5, 7 (sorted)
```

---

## Heap Complexity

```
Operation       | Time    | Proof
----------------|---------|------
Insert (push)   | O(log n)| Height of heap = log₂(n)
                |         | Bubble up at most h levels
Delete min (pop)| O(log n)| Bubble down at most h levels
Heapify         | O(n)    | Bottom-up bubble down
Find min        | O(1)    | Always at root
```

---

# GRAPH REPRESENTATION

## Graph - Formal Definition

**Definition:** A graph G = (V, E) consists of:
- V: Set of vertices (nodes)
- E: Set of edges (connections between vertices)

**Types:**
```
Directed:   A → B (one direction)
Undirected: A ↔ B (both directions)
Weighted:   Edge has value (distance, cost)
Unweighted: Edge has no value
```

---

## Adjacency Matrix

```python
# Undirected graph representation:
# Vertices: [0, 1, 2, 3]
# Edges: 0-1, 1-2, 2-3, 3-0

adj_matrix = [
    [0, 1, 0, 1],  # 0 connects to 1, 3
    [1, 0, 1, 0],  # 1 connects to 0, 2
    [0, 1, 0, 1],  # 2 connects to 1, 3
    [1, 0, 1, 0]   # 3 connects to 0, 2
]

# Check if edge exists: O(1)
has_edge = adj_matrix[0][1] == 1  # True

# Find all neighbors: O(V)
neighbors = [j for j in range(4) if adj_matrix[0][j] == 1]

# Space: O(V²)
```

---

## Adjacency List

```python
# Undirected graph representation:
adj_list = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

# Check if edge exists: O(degree)
has_edge = 1 in adj_list[0]  # True

# Find all neighbors: O(degree)
neighbors = adj_list[0]  # [1, 3]

# Space: O(V + E)
# Better for sparse graphs!
```

---

# COMPLEXITY COMPARISON

## Time Complexity Summary

| Operation | Array | Linked List | BST Avg | Hash Map | Heap |
|-----------|-------|-------------|---------|----------|------|
| Access | O(1) | O(n) | O(log n) | O(1) | O(1)* |
| Search | O(n) | O(n) | O(log n) | O(1) | O(n) |
| Insert | O(n) | O(n)** | O(log n) | O(1) | O(log n) |
| Delete | O(n) | O(n)** | O(log n) | O(1) | O(log n) |

*Heap access only top element (min/max)
**With pointer, O(1)

---

# CHOOSING DATA STRUCTURES

## Decision Tree

```
Need fast access by index?
├─ YES: Array/String
└─ NO: Continue

Need ordered data?
├─ YES: 
│  ├─ Access by key? Hash Map
│  ├─ Range queries? BST
│  └─ Frequent insertions? Linked List
└─ NO:
   ├─ Unique elements only? Set
   └─ Any elements? List

Need FIFO behavior?
├─ YES: Queue
└─ NO:
   ├─ Need LIFO? Stack
   ├─ Need min/max? Heap
   └─ Need graph? Adjacency List/Matrix
```

---

# WORKED EXAMPLES

## Example 1: Valid Palindrome using Two Pointers + Array

```python
def is_palindrome(s):
    """
    Check if string is palindrome (ignoring case and non-alphanumeric)
    
    Time: O(n) - single pass through string
    Space: O(1) - only use two pointers
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# Test:
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False
```

---

# INTERVIEW PREPARATION

## Q&A

**Q1: When would you use linked list instead of array?**
```
A: When:
- Frequent insertions/deletions at beginning O(1) vs O(n)
- Unknown size in advance (dynamic)
- Don't need random access

Avoid when:
- Need fast access O(1)
- Mostly read operations
- Space is limited (pointers take memory)
```

**Q2: What's the difference between hash map and BST?**
```
| Property | Hash Map | BST |
|----------|----------|-----|
| Access | O(1) avg | O(log n) |
| Order | No | Ordered |
| Range | No | Yes |
| Worst case | O(n) | O(n) |
| Use | Lookups | Sorted data |
```

**Q3: How does a heap maintain its property?**
```
A: Through bubble up/down operations:
- Insert: Add at end, bubble up (compare with parent)
- Delete: Remove root, move last to root, bubble down
- Both maintain heap property while minimizing moves
```

---

**Master all data structures. They're 40% of DSA interviews.** 🎯

