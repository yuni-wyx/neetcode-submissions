# Sliding Window: Variable-size window; frequency invariant

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
l = 0
counts = {}
best = 0
for r, x in enumerate(s):
    counts[x] = counts.get(x, 0) + 1
    while counts[x] > 1:
        counts[s[l]] -= 1
        l += 1
    best = max(best, r-l+1)
```

Complexity: O(n) time, O(k) space for distinct symbols.
