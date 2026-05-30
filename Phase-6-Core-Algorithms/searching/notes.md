# Searching Algorithms

## What is searching?
Finding a specific element inside a collection.
Like finding your name on an attendance list.

## Linear Search
Check every element one by one until found.
Simple but slow — O(n) time.
Works on ANY list — sorted or unsorted.
See: linear_search.py

## Binary Search  
Only works on SORTED lists.
Cut the search space in half every step.
Like guessing a number 1-100 by always 
guessing the middle.
O(log n) time — much faster for large inputs.
See: binary_search.py

## When to use which
Linear search → small list OR unsorted list
Binary search → large list AND sorted list

## Common mistake
Using binary search on an unsorted list 
gives wrong answers — always sort first.

## Practice problems
- Easy: Binary Search (LeetCode #704)
- Medium: Search in Rotated Array (LeetCode #33)
- Hard: Median of Two Sorted Arrays (LeetCode #4)
