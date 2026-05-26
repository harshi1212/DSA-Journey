# Phase 14 - Greedy Algorithms

## What is Greedy?

Making locally optimal choice at each step, hoping it leads to globally optimal solution.

**Visual**:
```
Problem: Pick maximum value path

Greedy approach: Always pick highest next value
  10 → 5 → 100  (total: 115) ✓ Works!

Sometimes greedy fails:
  5 → 100 → 1  (greedy picks 100)
  But 5 → 1 → 1000 (total: 1005) was better
```

---

## When Greedy Works

**Greedy Choice Property**: Locally optimal choice leads to globally optimal solution

**Optimal Substructure**: Optimal solution contains optimal solutions to subproblems

Both needed for greedy to work!

---

## Master These 4 Types

| Type | Example | Complexity |
|------|---------|-----------|
| **Activity Selection** | Schedule non-overlapping events | O(n log n) |
| **Interval Scheduling** | Merge/cover intervals | O(n log n) |
| **Huffman Coding** | Optimal compression | O(n log n) |
| **Classic Problems** | Gas station, candy, jump | O(n) |

---

## Key Insight

> "Greedy works when you can prove the greedy choice is always optimal"

Before using greedy:
1. Ask: Why is this locally optimal?
2. Prove: Does it stay globally optimal?
3. Test: Does it work on examples?

---

## Real-World Applications

- **Scheduling**: Event scheduling, CPU scheduling
- **Compression**: Huffman coding, data compression
- **Navigation**: Activity selection, resource allocation
- **Finance**: Fractional knapsack, min-coin change

---

## Greedy vs DP

| Aspect | Greedy | DP |
|--------|--------|-----|
| Speed | Faster (O(n)) | Slower (O(n²+)) |
| Guarantee | May fail | Always correct |
| When to use | When provably works | When unsure |
| Complexity | Easier to implement | Harder |

**Rule**: Try greedy first (faster). If it fails, use DP.
