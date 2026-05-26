"""
TEMPLATE: Segment Tree (Range Sum Query)
Use for: Range queries, point updates
Complexity: O(log n) per operation, O(n) build
"""

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            
            self.build(arr, left_node, start, mid)
            self.build(arr, right_node, mid + 1, end)
            
            self.tree[node] = self.tree[left_node] + self.tree[right_node]
    
    def update(self, idx, val, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1
        
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_node = 2 * node + 1
            right_node = 2 * node + 2
            
            if idx <= mid:
                self.update(idx, val, left_node, start, mid)
            else:
                self.update(idx, val, right_node, mid + 1, end)
            
            self.tree[node] = self.tree[left_node] + self.tree[right_node]
    
    def query(self, l, r, node=0, start=0, end=None):
        """Range sum query [l, r]"""
        if end is None:
            end = self.n - 1
        
        if r < start or l > end:
            return 0
        
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        p1 = self.query(l, r, left_node, start, mid)
        p2 = self.query(l, r, right_node, mid + 1, end)
        
        return p1 + p2

# Usage:
print("Template 7: Segment Tree")

arr = [1, 3, 5, 7, 9]
st = SegmentTree(arr)

print(f"Range sum [1, 3]: {st.query(1, 3)}")
st.update(2, 10)
print(f"After update index 2 to 10: {st.query(1, 3)}")
