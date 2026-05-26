"""
Trie Advanced
Word search, pattern matching, autocomplete with advanced features.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []  # All words with this prefix

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word and track all words at each node."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_list.append(word)
        node.is_word = True
    
    def search(self, word):
        """Exact word search."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word
    
    def starts_with(self, prefix):
        """Check if any word starts with prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def autocomplete(self, prefix):
        """Get all words with given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.word_list
    
    def word_search_board(self, board, word):
        """
        Search word in 2D board (WordSearch II style).
        Can move in 4 directions, can't reuse cells.
        """
        if not board or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, node, idx):
            if idx == len(word):
                return node.is_word
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            char = board[r][c]
            if char not in node.children or char == '#':
                return False
            
            # Mark as visited
            board[r][c] = '#'
            
            # Try 4 directions
            result = dfs(r+1, c, node.children[char], idx+1) or \
                    dfs(r-1, c, node.children[char], idx+1) or \
                    dfs(r, c+1, node.children[char], idx+1) or \
                    dfs(r, c-1, node.children[char], idx+1)
            
            # Restore cell
            board[r][c] = char
            
            return result
        
        # Start from each cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, self.root, 0):
                    return True
        
        return False

# Example 1: Basic Trie operations
print("=== Trie Advanced ===\n")

trie = Trie()
words = ["apple", "app", "application", "apply", "banana", "band"]

for word in words:
    trie.insert(word)

print("Dictionary:", words)
print(f"\nSearch 'apple': {trie.search('apple')}")  # True
print(f"Search 'app': {trie.search('app')}")  # True
print(f"Search 'appl': {trie.search('appl')}")  # False

print(f"\nStarts with 'app': {trie.starts_with('app')}")  # True
print(f"Starts with 'ban': {trie.starts_with('ban')}")  # True
print(f"Starts with 'cat': {trie.starts_with('cat')}")  # False

# Example 2: Autocomplete
print("\n=== Autocomplete ===\n")

suggestions = trie.autocomplete('app')
print(f"Suggestions for 'app': {suggestions}")

suggestions = trie.autocomplete('ba')
print(f"Suggestions for 'ba': {suggestions}")

suggestions = trie.autocomplete('z')
print(f"Suggestions for 'z': {suggestions}")

# Example 3: Word search in 2D board
print("\n=== Word Search in 2D Board ===\n")

board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v'],
]

trie2 = Trie()
search_words = ["oath", "pea", "eat", "rain"]

for word in search_words:
    trie2.insert(word)

print("Board:")
for row in board:
    print(' '.join(row))

print(f"\nWords to find: {search_words}")

for word in search_words:
    found = trie2.word_search_board([row[:] for row in board], word)
    print(f"  '{word}': {found}")

# Example 4: Spell checker
print("\n=== Spell Checker (Edit Distance 1) ===\n")

def spell_check(trie, word, max_distance=1):
    """Find words that differ by at most max_distance edits."""
    results = []
    
    def dfs(node, i, edits, current):
        if edits > max_distance:
            return
        
        if i == len(word):
            if node.is_word:
                results.append(current)
            return
        
        # Match character
        if word[i] in node.children:
            dfs(node.children[word[i]], i+1, edits, current + word[i])
        
        # Substitute (if edits available)
        if edits < max_distance:
            for char, child in node.children.items():
                if char != word[i]:
                    dfs(child, i+1, edits+1, current + char)
        
        # Delete from word (if edits available)
        if edits < max_distance:
            dfs(node, i+1, edits+1, current)
        
        # Insert into word (if edits available)
        if edits < max_distance:
            for char, child in node.children.items():
                dfs(child, i, edits+1, current + char)
    
    dfs(trie.root, 0, 0, "")
    return results

trie3 = Trie()
dictionary = ["cat", "car", "card", "care", "rat", "art", "bat"]
for word in dictionary:
    trie3.insert(word)

typo = "cat"
corrections = spell_check(trie3, typo, max_distance=1)
print(f"Corrections for '{typo}' (distance 1): {corrections}")

typo = "ca"
corrections = spell_check(trie3, typo, max_distance=1)
print(f"Corrections for '{typo}' (distance 1): {corrections}")

print("\n=== Complexity Analysis ===")
print("Insert:       O(m) - m = length of word")
print("Search:       O(m)")
print("Starts with:  O(m)")
print("Autocomplete: O(n) - n = number of words with prefix")
print("Board search: O(N * 4^L) - N = board size, L = word length")
print("Space:        O(ALPHABET_SIZE * N) - N = words inserted")
