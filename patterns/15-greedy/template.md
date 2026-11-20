# Greedy: Greedy; maintain invariant

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
reach = 0
for i, x in enumerate(nums):
    if i > reach: return False
    reach = max(reach, i+x)
return True
```

Complexity: O(n) time, O(1) space.
