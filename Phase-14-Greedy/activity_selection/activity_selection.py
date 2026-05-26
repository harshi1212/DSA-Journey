"""
Activity Selection - Select maximum non-overlapping activities
"""

def activity_selection(activities):
    """
    Select maximum number of non-overlapping activities.
    Greedy: Always pick activity ending earliest.
    """
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_end = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end:  # Non-overlapping
            selected.append((start, end))
            last_end = end
    
    return selected

# Example 1: Basic activity selection
print("=== Activity Selection ===\n")

activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8), (8, 9)]
print(f"Activities: {activities}")

selected = activity_selection(activities)
print(f"Selected: {selected}")
print(f"Count: {len(selected)}")  # 4

# Example 2: Verify greedy works
print("\n=== Verify Greedy is Optimal ===")
print("Sorted by end time:")
sorted_acts = sorted(activities, key=lambda x: x[1])
for act in sorted_acts:
    print(f"  {act}")

# Example 3: Weighted version (harder - requires DP)
print("\n=== Weighted Activity Selection (requires DP) ===")
weighted_activities = [
    (1, 3, 5),    # (start, end, value)
    (2, 5, 6),
    (4, 6, 5),
    (6, 7, 4),
    (5, 8, 11),
    (8, 9, 2),
]

print("With weights, greedy FAILS!")
print("Greedy (earliest end): (1,3,5) + (4,6,5) + (6,7,4) + (8,9,2) = 16")
print("Optimal (DP): (2,5,6) + (5,8,11) = 17")

# Example 4: Real-world - Meeting scheduling
print("\n=== Real-World: Meeting Scheduling ===")

meetings = [
    ("Team sync", 10, 11),
    ("1-on-1", 9, 10),
    ("Design review", 10, 12),
    ("Sprint planning", 14, 15),
    ("Retro", 11, 12),
]

# Convert to (start, end)
meetings_times = [(s, e) for _, s, e in meetings]
selected_idx = []

# Greedy selection
meetings_sorted = sorted(enumerate(meetings_times), key=lambda x: x[1][1])
selected = [meetings_sorted[0]]
last_end = meetings_sorted[0][1][1]

for idx, (start, end) in meetings_sorted[1:]:
    if start >= last_end:
        selected.append(((idx, (start, end))))
        last_end = end

print("Meetings (name, start, end):")
for name, s, e in meetings:
    print(f"  {name}: {s:00d}:00-{e:00d}:00")

print("\nOptimal schedule (non-overlapping):")
for idx, (s, e) in selected:
    print(f"  {meetings[idx][0]}: {s:00d}:00-{e:00d}:00")

print("\n=== Complexity ===")
print("Time:  O(n log n) - sorting dominates")
print("Space: O(1) - no extra space needed")
