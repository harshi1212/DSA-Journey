# Union-Find (Disjoint Set Union)

## What Is It?

A data structure that answers: "Are two items in the same group?"

**Visual**:
```
Initial:  1   2   3   4   5
          |   |   |   |   |
         {1} {2} {3} {4} {5}

Union(1,2):
          1-2  3   4   5
          |    |   |   |
         {1,2}{3}{4}{5}

Union(3,4):
          1-2  3-4  5
          |    |    |
         {1,2}{3,4}{5}

Connected(1,2)? YES
Connected(2,3)? NO
```

---

## Two Key Operations

1. **Union(a, b)** - Merge a's group with b's group
2. **Find(a)** - Which group does a belong to?

---

## Optimization Tricks

### Path Compression
When finding root, make nodes point directly to root.

```
Before:    After path compression:
  root           root
   |             /|\
   a      →     a b c
   |
   b
   |
   c
```

### Union by Rank
When merging groups, attach smaller tree under larger.

Prevents tall, skinny trees that are slow to traverse.

---

## Why It's Fast

- **Without optimizations**: O(n) per operation
- **With path compression**: O(log n) per operation
- **With both**: Nearly O(1) per operation (amortized)

This is the "nearly" in O(1)*!

---

## Problems It Solves

1. **Detect cycle in undirected graph**
   - Union edges: if Union fails, cycle exists

2. **Connected components**
   - Same as graph components but faster

3. **Friends circle**
   - Union friends: Find size of each group

4. **Network connectivity**
   - Which computers are reachable?
