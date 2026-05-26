# Project 3: Autocomplete Using Trie

## What does it do?

When user types characters, suggest possible words (like Google search suggestions).

**Real-world use**:
- Google search suggestions
- Mobile keyboard autocomplete
- IDE code completion
- Spell checkers

## Which DSA concepts does it use?

1. **Trie (Prefix Tree)** - Store words by prefix
2. **Tree traversal** - Find all words starting with prefix
3. **Recursion** - Build and search trie
4. **Sorting** - Rank suggestions by frequency

## How to run it

```bash
python solution.py
```

## Sample input and output

**Build trie with**: ["car", "cat", "card", "care", "dog"]

**User types**: `"ca"`  
**Suggestions**: `["car", "cat", "card", "care"]`

**User types**: `"do"`  
**Suggestions**: `["dog"]`

**User types**: `"ca"`  (typed "car" before)  
**Suggestions**: `["car", "cat", "card", "care"]` (ranked by frequency)

## What I learned

1. **Tries are perfect for prefix queries** - O(m) where m=length of word
2. **Frequency ranking matters** - Users want common words first
3. **Tree traversal finds all matches** - DFS to collect suggestions
4. **Character-by-character insertion** - Builds tree structure naturally
5. **Space-time tradeoff** - Uses more space for faster queries

## Variations to try

1. **Top-k suggestions**: Return only top-3 suggestions
2. **Edit distance**: Suggest similar words (typo correction)
3. **Recent words**: Track recency, not just frequency
4. **Context-aware**: Different suggestions based on previous word
5. **Multi-language**: Support multiple languages

## How Autocomplete Actually Works

Real systems like Google:
1. **Precompute** all searches into a Trie
2. **Rank** by frequency globally
3. **Personalize** based on user history
4. **Serve** suggestions in milliseconds
5. **Update** daily with new searches

Our simple version shows the core idea!
