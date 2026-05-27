# Phase 12 - Advanced Data Structures (Master Guide)

**Specialized structures for specific problem patterns.**

---

## Trie (Prefix Tree)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Time: O(m) where m = word length"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
    
    def search(self, word):
        """Time: O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
    def startsWith(self, prefix):
        """Time: O(m)"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

---

## Segment Tree

```python
class SegmentTree:
    def __init__(self, arr):
        """Build segment tree - Time: O(n)"""
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, L, R):
        """Range sum query - Time: O(log n)"""
        return self._query_helper(0, 0, self.n - 1, L, R)
    
    def _query_helper(self, node, start, end, L, R):
        if R < start or end < L:
            return 0
        
        if L <= start and end <= R:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self._query_helper(2*node+1, start, mid, L, R)
        right_sum = self._query_helper(2*node+2, mid+1, end, L, R)
        
        return left_sum + right_sum
    
    def update(self, idx, val):
        """Point update - Time: O(log n)"""
        self._update_helper(0, 0, self.n - 1, idx, val)
    
    def _update_helper(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update_helper(2*node+1, start, mid, idx, val)
            else:
                self._update_helper(2*node+2, mid+1, end, idx, val)
            
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
```

---

## Binary Indexed Tree (Fenwick Tree)

```python
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, idx, delta):
        """Time: O(log n)"""
        idx += 1  # 1-indexed
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)
    
    def query(self, idx):
        """Prefix sum [0, idx] - Time: O(log n)"""
        idx += 1  # 1-indexed
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result
    
    def range_query(self, left, right):
        """Range sum [left, right] - Time: O(log n)"""
        if left == 0:
            return self.query(right)
        return self.query(right) - self.query(left - 1)
```

---

## Balanced BST (AVL Tree)

```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Time: O(log n)"""
        self.root = self._insert(self.root, val)
    
    def _insert(self, node, val):
        if not node:
            return AVLNode(val)
        
        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)
        
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        
        return self._balance(node)
    
    def _get_height(self, node):
        return node.height if node else 0
    
    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _balance(self, node):
        balance = self._get_balance(node)
        
        # Left heavy
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right heavy
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        left_child.height = 1 + max(self._get_height(left_child.left),
                                    self._get_height(left_child.right))
        
        return left_child
    
    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))
        right_child.height = 1 + max(self._get_height(right_child.left),
                                     self._get_height(right_child.right))
        
        return right_child
```

---

## Monotonic Stack

```python
def daily_temperatures(temperatures):
    """
    Find next warmer temperature for each day
    
    Time: O(n)
    Space: O(n)
    """
    result = [0] * len(temperatures)
    stack = []  # indices in decreasing order of temperature
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx
        
        stack.append(i)
    
    return result

# Example: [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
```

---

## Monotonic Deque

```python
from collections import deque

def maxSlidingWindow(nums, k):
    """
    Find max in every sliding window
    
    Time: O(n)
    Space: O(k)
    """
    result = []
    dq = deque()  # Store indices in decreasing order of values
    
    for i, num in enumerate(nums):
        # Remove elements outside window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Example: [1,3,-1,-3,5,3,6,7], k=3
# Output: [3,3,5,5,6,7]
```

---

## Suffix Array

```python
def suffix_array(s):
    """
    Create suffix array
    Time: O(n log² n)
    """
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    
    return [idx for _, idx in suffixes]

# Example: "banana"
# Suffixes: "banana", "anana", "nana", "ana", "na", "a"
# Sorted: "a", "ana", "anana", "banana", "na", "nana"
# SA: [5, 3, 1, 0, 4, 2]
```

---

## Skip List

```python
import random

class SkipListNode:
    def __init__(self, val, level):
        self.val = val
        self.forward = [None] * level

class SkipList:
    def __init__(self):
        self.max_level = 16
        self.header = SkipListNode(None, self.max_level)
        self.level = 1
    
    def search(self, target):
        """Time: O(log n) average"""
        node = self.header
        
        for i in range(self.level - 1, -1, -1):
            while node.forward[i] and node.forward[i].val < target:
                node = node.forward[i]
        
        node = node.forward[0]
        
        return node and node.val == target
    
    def add(self, val):
        """Time: O(log n) average"""
        update = [None] * self.max_level
        node = self.header
        
        for i in range(self.level - 1, -1, -1):
            while node.forward[i] and node.forward[i].val < val:
                node = node.forward[i]
            update[i] = node
        
        level = self._random_level()
        
        if level > self.level:
            for i in range(self.level, level):
                update[i] = self.header
            self.level = level
        
        new_node = SkipListNode(val, level)
        
        for i in range(level):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
    
    def _random_level(self):
        level = 1
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level
```

---

## LRU Cache (Advanced Implementation)

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove oldest
```

---

**Master advanced structures for competitive programming.** 🎯

