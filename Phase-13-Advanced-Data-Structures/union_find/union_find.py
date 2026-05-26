"""
Union-Find (Disjoint Set Union)
Efficiently detect connectivity and merge groups.
"""

class UnionFind:
    """Union-Find data structure with path compression and union by rank."""
    
    def __init__(self, n):
        """Initialize n disjoint sets."""
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
    
    def find(self, x):
        """
        Find the root of x's group.
        Path compression: make x point directly to root.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        """
        Union x's group with y's group.
        Union by rank: attach smaller tree under larger.
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False  # Already in same group
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]
        
        return True
    
    def connected(self, x, y):
        """Check if x and y are in same group."""
        return self.find(x) == self.find(y)
    
    def get_size(self, x):
        """Get size of x's group."""
        return self.size[self.find(x)]

# Example 1: Basic usage
print("=== Union-Find Basics ===\n")

uf = UnionFind(6)

print("Initial state: {0} {1} {2} {3} {4} {5}")

# Union operations
uf.union(0, 1)
uf.union(1, 2)
print("After union(0,1), union(1,2):")
print(f"  Connected(0,2)? {uf.connected(0, 2)}")  # True

uf.union(3, 4)
print("After union(3,4):")
print(f"  Connected(0,3)? {uf.connected(0, 3)}")  # False

uf.union(2, 4)
print("After union(2,4):")
print(f"  Connected(0,3)? {uf.connected(0, 3)}")  # True

# Example 2: Cycle detection
print("\n=== Cycle Detection ===\n")

def has_cycle(edges, num_nodes):
    """Detect cycle using Union-Find."""
    uf = UnionFind(num_nodes)
    
    for u, v in edges:
        # If u and v already connected, adding edge creates cycle
        if not uf.union(u, v):
            return True
    
    return False

edges = [(0, 1), (1, 2), (2, 0)]  # Triangle = cycle
print(f"Edges: {edges}")
print(f"Has cycle? {has_cycle(edges, 3)}")  # True

edges = [(0, 1), (1, 2), (2, 3)]  # Tree = no cycle
print(f"\nEdges: {edges}")
print(f"Has cycle? {has_cycle(edges, 4)}")  # False

# Example 3: Connected components
print("\n=== Connected Components ===\n")

def find_components(edges, num_nodes):
    """Find all connected components."""
    uf = UnionFind(num_nodes)
    
    for u, v in edges:
        uf.union(u, v)
    
    # Group nodes by root
    components = {}
    for node in range(num_nodes):
        root = uf.find(node)
        if root not in components:
            components[root] = []
        components[root].append(node)
    
    return list(components.values())

edges = [(0, 1), (2, 3), (4, 5), (5, 6)]
components = find_components(edges, 7)
print(f"Edges: {edges}")
print(f"Components: {components}")  # [[0,1], [2,3], [4,5,6]]

# Example 4: Friends circle
print("\n=== Friends Circle ===\n")

def largest_friend_circle(friends, num_people):
    """Find size of largest friend circle."""
    uf = UnionFind(num_people)
    
    for person1, person2 in friends:
        uf.union(person1, person2)
    
    # Find largest group
    max_size = 0
    for person in range(num_people):
        max_size = max(max_size, uf.get_size(person))
    
    return max_size

friendships = [
    (0, 1),  # 0-1 are friends
    (1, 2),  # 1-2 are friends
    (3, 4),  # 3-4 are friends
    (5, 6),  # 5-6 are friends
    (6, 7),  # 6-7 are friends
]

size = largest_friend_circle(friendships, 8)
print(f"Friendships: {friendships}")
print(f"Largest circle size: {size}")  # 4 (group: 5,6,7 + ?)

# Example 5: Redundant connections
print("\n=== Redundant Connection ===\n")

def find_redundant_edge(edges):
    """Find an edge that creates a cycle."""
    num_nodes = len(edges)
    uf = UnionFind(num_nodes + 1)
    
    for u, v in edges:
        if not uf.union(u, v):
            return (u, v)  # This edge creates cycle
    
    return None

edges = [(1, 2), (2, 3), (3, 1)]  # Triangle
redundant = find_redundant_edge(edges)
print(f"Edges: {edges}")
print(f"Redundant edge: {redundant}")  # (3, 1)

print("\n=== Complexity Analysis ===")
print("Union:     O(α(n)) ≈ O(1)")
print("Find:      O(α(n)) ≈ O(1)")
print("Connected: O(α(n)) ≈ O(1)")
print("\nα(n) = inverse Ackermann function (grows extremely slowly)")
print("For all practical purposes: O(1)")
