# Phase 15 - String Algorithms

## Why String Algorithms Matter?

Substring/pattern matching is fundamental:
- Search engines (find keywords in pages)
- DNA sequencing (find patterns in genes)
- Plagiarism detection (find copied text)
- Text editors (find & replace)

---

## Naive vs Optimized

| Approach | Time | Space | When |
|----------|------|-------|------|
| **Brute Force** | O(n*m) | O(1) | Small strings |
| **KMP** | O(n+m) | O(m) | General purpose |
| **Z-Algorithm** | O(n+m) | O(n) | Prefix problems |
| **Rabin-Karp** | O(n+m)* | O(1) | Multiple patterns |

*Worst case: O(n*m), but usually O(n+m)

---

## Master These 3 Algorithms

| Algorithm | Best For | Complexity | Use Case |
|-----------|----------|-----------|----------|
| **KMP** | Single pattern matching | O(n+m) | Find substring, implement strStr() |
| **Z-Algorithm** | Prefix/period detection | O(n+m) | Count occurrences, find periods |
| **Rabin-Karp** | Multiple patterns | O(n+m) | Find many patterns, 2D patterns |

---

## Real-World Applications

- **Search engines**: Find keywords in billions of pages (Rabin-Karp)
- **DNA matching**: Find genes in genome sequences (KMP)
- **Plagiarism detection**: Find copied text in corpus (Rabin-Karp)
- **Spell checkers**: Find similar strings (Z-algorithm)
- **Compression**: LZ77 uses string matching (KMP)

---

## Core Insight

**Preprocessing wins**: Spend time analyzing pattern to avoid re-scanning

- **KMP**: Build failure function from pattern
- **Z-algorithm**: Build Z-array from combined string
- **Rabin-Karp**: Hash pattern once, compare hashes
