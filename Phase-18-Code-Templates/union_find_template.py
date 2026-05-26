"""
TEMPLATE: Union-Find (Disjoint Set Union)
Use for: Connected components, cycle detection, MST
Complexity: Nearly O(1) per operation with path compression
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank"""
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_size(self, x):
        return self.size[self.find(x)]

# Usage:
# uf = UnionFind(n)
# uf.union(a, b)
# if uf.is_connected(x, y): ...

print("=== Code Templates ===\n")
print("Template 1: Union-Find")

uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print(f"0-2 connected? {uf.is_connected(0, 2)}")  # True
print(f"0-3 connected? {uf.is_connected(0, 3)}")  # False
