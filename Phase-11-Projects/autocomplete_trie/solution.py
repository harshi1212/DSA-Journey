"""
Project 3: Autocomplete Using Trie

WHAT DOES IT DO:
Build autocomplete that suggests words as user types.
Example: User types "ca" → suggests "car", "cat", "can"

WHICH DSA CONCEPTS:
1. Trie (prefix tree - stores words by prefix)
2. Tree traversal (find all words with prefix)
3. Recursion (build trie, search trie)

HOW TO RUN:
python solution.py

SAMPLE INPUT:
Trie with: ["car", "cat", "card", "care", "dog", "dodge"]
Query: "ca" → Returns: ["car", "cat", "card", "care"]
Query: "do" → Returns: ["dog", "dodge"]
Query: "ca" → Ranked by frequency
"""

class TrieNode:
    """Node in a Trie."""
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_word = False    # Is this a complete word?
        self.frequency = 0      # How many times seen?

class Trie:
    """Trie for autocomplete."""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word into trie."""
        node = self.root
        
        # Traverse or create path for each character
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        # Mark end of word, increase frequency
        node.is_word = True
        node.frequency += 1
    
    def search(self, prefix):
        """Find all words with given prefix."""
        node = self.root
        
        # Navigate to end of prefix
        for char in prefix:
            if char not in node.children:
                return []  # Prefix not found
            node = node.children[char]
        
        # Find all words starting from this node
        results = []
        self._dfs(node, prefix, results)
        
        # Sort by frequency (most common first)
        results.sort(key=lambda x: -x[1])
        return [word for word, _ in results]
    
    def _dfs(self, node, prefix, results):
        """Depth-first search to find all words."""
        # If this is a word, add to results
        if node.is_word:
            results.append((prefix, node.frequency))
        
        # Recursively search all children
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, results)

# ── Test cases ────────────────────────────

trie = Trie()

# Insert words
words = ["car", "cat", "card", "care", "dog", "dodge", "apple", "app"]
for word in words:
    trie.insert(word)
    trie.insert(word)  # Insert twice to increase frequency

# Test searches
test_queries = [
    ("ca", ["car", "cat", "card", "care"]),
    ("do", ["dog", "dodge"]),
    ("ap", ["app", "apple"]),
    ("c", ["car", "cat", "card", "care"]),
    ("z", []),  # Not found
]

print("Autocomplete Trie Tests:")
for prefix, expected_approx in test_queries:
    results = trie.search(prefix)
    # Just check if all expected words are in results
    all_found = all(word in results for word in expected_approx)
    status = "✓" if all_found else "✗"
    print(f"{status} \"{prefix}\" → {results[:3]}...")  # Show first 3

# COMPLEXITY
print("\n=== COMPLEXITY ANALYSIS ===")
print("Insert:  O(m) - m = length of word")
print("Search:  O(n + k log k) - n = nodes visited, k = results, sort")
print("Space:   O(m * n) - m = average word length, n = number of words")
