# Activity Selection Problem

## What is it?

Select maximum number of non-overlapping activities.

```
Activities (start, end):
  (1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)

Greedy choice: Always pick activity ending earliest
  Pick (1, 3) → leaves most room
  Pick (4, 6) → leaves most room
  Pick (6, 7) → leaves most room
  Pick (8, 9) → leaves most room
  
Result: 4 activities
```

**Why greedy works**: Ending earliest leaves maximum room for future activities

---

## Algorithm

1. Sort activities by end time
2. Always select activity ending earliest
3. Repeat until no more activities fit

**Proof**: If optimal solution doesn't pick earliest ending, swap it in = still optimal

---

## Code

```python
def activity_selection(activities):
    # Sort by end time (greedy choice)
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_end = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end:  # Non-overlapping
            selected.append((start, end))
            last_end = end
    
    return selected
```

**Complexity**: O(n log n) - sorting dominates
