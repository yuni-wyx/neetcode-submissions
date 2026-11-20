# Binary Search: Binary search; monotonic feasibility

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
l, r = 0, len(nums)-1
while l <= r:
    m = (l+r)//2
    if nums[m] == target: return m
    if nums[m] < target: l = m+1
    else: r = m-1
return -1
```

Complexity: O(log n) time, O(1) space.
