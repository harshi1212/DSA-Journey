"""
Segment Tree
Efficient range queries (sum, min, max) with updates.
"""

class SegmentTree:
    """Segment Tree for range sum queries and point updates."""
    
    def __init__(self, arr):
        """Build segment tree from array."""
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 4*n is safe upper bound
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        """Recursively build tree."""
        if start == end:
            # Leaf node
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            # Build left and right subtrees
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            
            # Parent = sum of children
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def update(self, idx, val):
        """Update element at index idx to val."""
        self._update(0, 0, self.n - 1, idx, val)
    
    def _update(self, node, start, end, idx, val):
        """Recursively update tree."""
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            if idx <= mid:
                self._update(left_child, start, mid, idx, val)
            else:
                self._update(right_child, mid + 1, end, idx, val)
            
            # Update parent
            self.tree[node] = self.tree[left_child] + self.tree[right_child]
    
    def query(self, L, R):
        """Query sum from index L to R (inclusive)."""
        return self._query(0, 0, self.n - 1, L, R)
    
    def _query(self, node, start, end, L, R):
        """Recursively query sum in range."""
        if R < start or L > end:
            # No overlap
            return 0
        
        if L <= start and end <= R:
            # Complete overlap
            return self.tree[node]
        
        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_sum = self._query(left_child, start, mid, L, R)
        right_sum = self._query(right_child, mid + 1, end, L, R)
        
        return left_sum + right_sum

# Example 1: Basic usage
print("=== Segment Tree: Range Sum ===\n")

arr = [1, 5, 2, 2, 8, 3]
st = SegmentTree(arr)

print(f"Array: {arr}")
print(f"Query(0, 2): {st.query(0, 2)}")  # 1+5+2 = 8
print(f"Query(2, 4): {st.query(2, 4)}")  # 2+2+8 = 12
print(f"Query(0, 5): {st.query(0, 5)}")  # Sum of all = 21

print("\nAfter update(2, 10):")
st.update(2, 10)  # Change arr[2] from 2 to 10
print(f"Query(0, 2): {st.query(0, 2)}")  # 1+5+10 = 16
print(f"Query(0, 5): {st.query(0, 5)}")  # New sum = 29

# Example 2: Multiple operations
print("\n=== Multiple Operations ===\n")

arr = [3, 8, 6, 7]
st = SegmentTree(arr)

operations = [
    ("query", 0, 2),  # 3+8+6 = 17
    ("update", 1, 5), # arr[1] = 5
    ("query", 0, 3),  # 3+5+6+7 = 21
    ("update", 0, 2), # arr[0] = 2
    ("query", 0, 3),  # 2+5+6+7 = 20
]

for op in operations:
    if op[0] == "query":
        result = st.query(op[1], op[2])
        print(f"Query({op[1]}, {op[2]}): {result}")
    else:
        st.update(op[1], op[2])
        print(f"Update({op[1]}, {op[2]})")

# Example 3: Range Maximum Query
print("\n=== Range Maximum Query (Different Aggregate) ===\n")

class MaxSegmentTree(SegmentTree):
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            
            # Parent = max of children (not sum)
            self.tree[node] = max(self.tree[left_child], self.tree[right_child])
    
    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            if idx <= mid:
                self._update(left_child, start, mid, idx, val)
            else:
                self._update(right_child, mid + 1, end, idx, val)
            
            self.tree[node] = max(self.tree[left_child], self.tree[right_child])
    
    def _query(self, node, start, end, L, R):
        if R < start or L > end:
            return float('-inf')
        
        if L <= start and end <= R:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        
        left_max = self._query(left_child, start, mid, L, R)
        right_max = self._query(right_child, mid + 1, end, L, R)
        
        return max(left_max, right_max)

arr = [3, 8, 6, 7, 4]
mst = MaxSegmentTree(arr)

print(f"Array: {arr}")
print(f"Max(0, 2): {mst.query(0, 2)}")  # max(3,8,6) = 8
print(f"Max(1, 4): {mst.query(1, 4)}")  # max(8,6,7,4) = 8

mst.update(2, 10)  # arr[2] = 10
print(f"After update(2, 10):")
print(f"Max(0, 2): {mst.query(0, 2)}")  # max(3,8,10) = 10

print("\n=== Complexity Analysis ===")
print("Build:  O(n)")
print("Query:  O(log n)")
print("Update: O(log n)")
print("Space:  O(n)")
