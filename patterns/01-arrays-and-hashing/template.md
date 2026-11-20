# Arrays & Hashing: Hash map / set; frequency counting; prefix products

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
```

Complexity: O(n) time, O(n) space.
