# 1-D Dynamic Programming: 1-D DP; state transition

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
    dp[i] = dp[i-1]
    if i >= 2: dp[i] += dp[i-2]
```

Complexity: O(n) time, O(n) space; rolling variables possible.
