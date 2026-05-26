# Phase 5.6 - Heaps

## What is it?

A heap is a special binary tree where parent ≤ children (min-heap) or parent ≥ children (max-heap).

```
Min Heap:
       1
      / \
     2   3
    / \
   4   5

Max Heap:
       10
      /  \
     9    8
    / \
   7   6
```

Why study them?
- Efficient priority queues
- Finding min/max in O(log n)
- Used in Dijkstra's algorithm
- Interview medium problems

---

## Why does it matter?

**Real-world reasons:**
1. **Priority queues** - Hospital triage (urgent cases first)
2. **Scheduling** - OS processes by priority
3. **Graph algorithms** - Dijkstra uses heap
4. **Stream processing** - Find kth largest/smallest
5. **Interview questions** - "Top k elements"

---

## Practice Problems

- Easy: [Last Stone Weight — LeetCode #1046](https://leetcode.com/problems/last-stone-weight/)
- Medium: [Kth Largest Element in an Array — LeetCode #215](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- Medium: [Merge K Sorted Lists — LeetCode #23](https://leetcode.com/problems/merge-k-sorted-lists/)
