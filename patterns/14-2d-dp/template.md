# 2-D Dynamic Programming: 2-D DP; grid/string prefixes

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if a[i-1] == b[j-1]: dp[i][j] = 1+dp[i-1][j-1]
        else: dp[i][j] = max(dp[i-1][j],dp[i][j-1])
```

Complexity: O(m*n) time and space.
