# Two Pointers: Opposite-end pointers; sorted pair search

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
l, r = 0, len(nums)-1
while l < r:
    s = nums[l] + nums[r]
    if s == target: return l, r
    if s < target: l += 1
    else: r -= 1
```

Complexity: O(n) time, O(1) space.
