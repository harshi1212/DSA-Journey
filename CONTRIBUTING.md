# Contributing to DSA Journey

## Daily Commit Workflow

This repository maintains a consistent commit history to track learning progress. After each study session or work session, please follow these guidelines.

### After Every Study Session

```bash
git add .
git commit -m "📚 Phase [X]: studied [topic]"
```

**Example:**
```bash
git commit -m "📚 Phase 1: studied Python basics - loops, functions, list comprehensions"
```

---

### After Solving a Practice Problem

```bash
git add .
git commit -m "✅ Solved: [problem name] — [pattern used]"
```

**Example:**
```bash
git commit -m "✅ Solved: Two Sum — Hash Map pattern"
git commit -m "✅ Solved: LRU Cache — Design pattern with Doubly Linked List + Hash Map"
```

---

### After Adding or Updating Notes

```bash
git add .
git commit -m "📝 Notes: [topic] — [key concept added]"
```

**Example:**
```bash
git commit -m "📝 Notes: Graph algorithms — added BFS implementation explanation"
```

---

### After Fixing a Bug or Issue

```bash
git add .
git commit -m "🔧 Fix: [what was fixed]"
```

**Example:**
```bash
git commit -m "🔧 Fix: corrected time complexity analysis in sorting guide"
```

---

### After Completing a Phase

```bash
git add .
git commit -m "🎓 Phase [X] Complete: [phase name]"
```

**Example:**
```bash
git commit -m "🎓 Phase 7 Complete: Algorithm Patterns - Two Pointers, Sliding Window, DP, Backtracking"
```

---

## Commit Message Guidelines

### Format
```
[emoji] [Action]: [What you did] — [Optional context]
```

### Allowed Emojis
- 📚 Learning/studying a topic
- ✅ Solved a problem
- 📝 Added/updated notes
- 🔧 Fixed a bug or issue
- 🎓 Completed a phase
- ✨ Added new feature/improvement
- 📊 Updated documentation

### Best Practices
1. **Commit frequently** — Aim for at least 1 commit per study day
2. **Write clear messages** — Future you will thank you
3. **Keep it concise** — One line for the main message
4. **Be specific** — Say which algorithm, problem, or topic
5. **Use emoji** — Makes history more readable

---

## Typical Daily Commit Pattern

```bash
# After studying Phase 5 topics
git add .
git commit -m "📚 Phase 5: studied hash maps and sets — dict operations and complexity"

# After solving a problem
git add .
git commit -m "✅ Solved: Valid Palindrome — Two Pointers pattern"

# After optimizing code
git add .
git commit -m "✨ Optimization: reduced palindrome checker from O(n²) to O(n) using two pointers"
```

---

## Push to GitHub

After making local commits, push to the remote repository:

```bash
git push origin main
```

This keeps your GitHub profile active and backs up your work.

---

## Repository Health

Following this workflow helps maintain:
- ✅ Clear learning history
- ✅ Regular commit streaks
- ✅ Easy progress tracking
- ✅ GitHub profile contributions
- ✅ Backup of your work

Happy learning! 🚀
