# Stack: Stack; monotonic decreasing stack

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
stack = []
ans = [0] * len(nums)
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        j = stack.pop()
        ans[j] = i-j
    stack.append(i)
```

Complexity: O(n) time, O(n) space.
