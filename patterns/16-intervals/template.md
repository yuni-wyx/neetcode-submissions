# Intervals: Sort and sweep

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
merged = []
for a,b in sorted(intervals):
    if not merged or a > merged[-1][1]: merged.append([a,b])
    else: merged[-1][1] = max(merged[-1][1], b)
```

Complexity: O(n log n) time, O(n) output space.
