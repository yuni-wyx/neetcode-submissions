# Backtracking: Backtracking; choose/explore/undo

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
ans, path = [], []
def dfs(start):
    ans.append(path.copy())
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(i+1)
        path.pop()
dfs(0)
```

Complexity: O(n*2^n) output time, O(n) recursion excluding output.
