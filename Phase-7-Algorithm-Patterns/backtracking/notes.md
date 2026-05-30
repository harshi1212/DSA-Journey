# Backtracking

## What is it?
Try all possibilities. When you hit a dead end
go back and try something else.
Like solving a maze — go forward, blocked,
come back, try another path.

## The template — always the same
def backtrack(choices, path, result):
    if goal reached:
        result.append(path copy)
        return
    for choice in choices:
        make the choice      # add to path
        backtrack(...)       # go deeper
        undo the choice      # remove from path

## The three steps
1. Choose — pick an option
2. Explore — recurse with that choice
3. Unchoose — undo the choice (backtrack)

## When to use
- Generate all permutations or combinations
- Solve puzzles (Sudoku, N-Queens)
- Find all valid paths

## Common mistake
Forgetting to undo the choice before
moving to the next option.
path.pop() is as important as path.append()

## Practice problems
- Easy: Subsets (LeetCode #78)
- Medium: Permutations (LeetCode #46)
- Hard: N-Queens (LeetCode #51)
