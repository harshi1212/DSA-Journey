# Trie Advanced

## What Can Advanced Tries Do?

| Operation | Basic Trie | Advanced Trie |
|-----------|-----------|---------------|
| Exact search | ✓ | ✓ |
| Prefix search | ✓ | ✓ |
| **Word search in 2D board** | ✗ | ✓ |
| **Spell checking** | ✗ | ✓ |
| **Pattern matching** | ✗ | ✓ |

---

## Problems It Solves

### 1. **Autocomplete with Filtering**
- Return all words with prefix
- Filter by frequency
- Sort by relevance

### 2. **Word Search in 2D Grid (WordSearch II)**
- Find all valid words in grid
- Move in 4 directions
- Can't reuse cells

### 3. **Spell Checker**
- Find words with edit distance 1
- Suggest corrections
- Handle typos

### 4. **Dictionary with Wildcards**
- Search patterns like "a.c" where . is any character
- Regular expression matching

---

## Advanced Features

**Tracking word list at each node**:
```python
node.word_list = [words_with_this_prefix]
```

This allows:
- O(1) retrieval of all words with prefix
- Fast autocomplete
- Frequency sorting

**DFS for 2D board search**:
- Traverse board in 4 directions
- Mark visited cells
- Restore on backtrack

---

## When to Use

- Autocomplete systems
- Spell checkers
- Puzzle solvers (word games)
- Dictionary lookups with constraints
