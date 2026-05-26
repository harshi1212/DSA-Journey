# Project 1: Word Frequency Counter

## What does it do?

Read a text file, count how many times each word appears, show the most common words.

**Real-world use**: 
- Google analyzes page content to understand topics
- Twitter finds trending words
- Content moderation (find common spam words)

## Which DSA concepts does it use?

1. **Hash Map** - Count words (word → frequency)
2. **Sorting** - Sort by frequency
3. **String processing** - Parse words from text
4. **File I/O** - Read files

## How to run it

```bash
python solution.py
```

## Sample input and output

**Input file (sample.txt)**:
```
The quick brown fox jumps over the lazy dog.
The dog was very lazy.
The fox was quick and clever.
```

**Output**:
```
Top 5 most common words:
  the: 3
  lazy: 2
  fox: 2
  quick: 2
  dog: 2
```

## What I learned

1. **Hash maps are powerful for counting** - O(1) lookup and update
2. **Sorting enables ranking** - Most common = highest frequency
3. **Regex for word extraction** - Split on boundaries, not spaces
4. **File handling is common** - Real programs read files
5. **Lowercase normalization** - "The" and "the" should be same word

## Variations to try

1. **Ignore common words**: Filter out "the", "a", "an"
2. **N-grams**: Count "the quick" as 2-gram
3. **Case sensitive**: Keep original case
4. **Include bigrams**: Count pairs of words
5. **Time-based**: Count words by hour/day for trends
