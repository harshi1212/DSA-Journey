# Sorting Algorithms

## What is sorting?
Arranging elements in a specific order.
Like arranging books alphabetically on a shelf.

## Bubble Sort — O(n²)
Compare adjacent pairs and swap if out of order.
Repeat until no swaps needed.
Slow — only good for understanding, 
never use in real code.
See: bubble_sort.py

## Merge Sort — O(n log n)
Split array in half, sort each half, merge back.
Uses recursion — divide and conquer.
This is what Python uses internally.
Stable sort — equal elements keep their order.
See: merge_sort.py

## Quick Sort — O(n log n) average
Pick a pivot, put smaller elements left,
larger elements right. Repeat recursively.
Very fast in practice.
See: quick_sort.py

## When to use which
In interviews: always use arr.sort() unless 
asked to implement from scratch.
In questions: merge sort is safest to implement.

## Common mistake
Bubble sort on large inputs will time out.
Never use it for anything serious.

## Practice problems
- Easy: Sort Colors (LeetCode #75)
- Medium: Kth Largest Element (LeetCode #215)
- Hard: Count of Smaller Numbers (LeetCode #315)
