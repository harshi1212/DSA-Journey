# Segment Tree

## What Is It?

A binary tree where each node stores aggregate info (sum, min, max) of a range.

**Example** (Sum Segment Tree):
```
         [10]           (sum of 1-4)
        /    \
      [6]    [4]       (sum of 1-2, 3-4)
      / \    / \
    [1][5][2][2]      (individual elements: 1,5,2,2)
```

---

## Operations

1. **Build** - O(n) - Create tree from array
2. **Query** - O(log n) - Sum/min/max of range [L, R]
3. **Update** - O(log n) - Change one element, update tree

---

## Why Not Use Simple Array?

| Operation | Array | Segment Tree |
|-----------|-------|--------------|
| Update | O(1) | O(log n) |
| Query | O(n) | O(log n) |
| **Both** | Slow | Fast |

Segment Tree wins when you have **many updates AND many queries**.

---

## When to Use

- **Range queries with updates**: Sum/min/max of range, then update element
- **Competitive programming**: Heavy duty range operations
- **Database indexes**: Fast queries on changing data

---

## Alternatives

- **Fenwick Tree**: Similar, but simpler to code, O(log n)
- **Square Root Decomposition**: Simpler, O(√n)
- **Lazy Propagation**: For range updates (not point updates)
