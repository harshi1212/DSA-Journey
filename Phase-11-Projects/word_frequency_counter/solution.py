"""
Project 1: Word Frequency Counter

WHAT DOES IT DO:
Read a text file, count frequency of each word, display top-N most common words.

WHICH DSA CONCEPTS:
1. Hash Map (word -> count)
2. Sorting (sort by frequency)
3. Strings (parsing words)
4. File I/O (read file)

HOW TO RUN:
python solution.py

SAMPLE INPUT:
"The quick brown fox jumps over the lazy dog. The dog was lazy."

SAMPLE OUTPUT:
the: 2
lazy: 2
dog: 2
quick: 1
...
"""

def word_frequency_counter(filename, top_n=5):
    """
    Count word frequencies in a file.
    Return top_n most common words.
    """
    # Step 1: Read file and collect all words
    # Why: Need all words before counting
    try:
        with open(filename, 'r') as f:
            text = f.read().lower()  # Lowercase for consistency
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return []
    
    # Step 2: Clean and split into words
    # Why: Remove punctuation, split by spaces
    import re
    words = re.findall(r'\b[a-z]+\b', text)  # Only alphanumeric words
    
    # Step 3: Count frequencies using hash map
    # Why: O(1) lookup and update
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Step 4: Sort by frequency (descending)
    # Why: Find most common words
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Step 5: Return top-n
    return sorted_words[:top_n]

# ── Test with sample ────────────────────────────

# Create sample file
sample_text = """
The quick brown fox jumps over the lazy dog.
The dog was very lazy.
The fox was quick and clever.
"""

with open('sample.txt', 'w') as f:
    f.write(sample_text)

# Run counter
print("Top 5 most common words:")
result = word_frequency_counter('sample.txt', top_n=5)
for word, count in result:
    print(f"  {word}: {count}")

# ANALYSIS
print("\n=== COMPLEXITY ANALYSIS ===")
print("Time:  O(n log n) - n words, sorting dominates")
print("Space: O(n) - hash map stores unique words")
