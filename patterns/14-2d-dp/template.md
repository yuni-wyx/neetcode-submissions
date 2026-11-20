# 2-D Dynamic Programming — Interview patterns

## Recognition
Two sequences or grid states

## Decision rules
Define dp[i][j], initialize base row/column, fill dependency order.

## Python reference: lcs

```python
def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i, x in enumerate(a, 1):
        for j, y in enumerate(b, 1):
            dp[i][j] = dp[i-1][j-1] + 1 if x == y else max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
```

O(mn) time and space.

## Common pitfalls
Avoid aliased rows; interval DP may require increasing length instead.

## Representative problems
- LC 62: [Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium)
- LC 1143: [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (Medium)
- LC 309: [Best Time to Buy And Sell Stock With Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) (Medium)
- LC 518: [Coin Change II](https://leetcode.com/problems/coin-change-ii/) (Medium)
- LC 494: [Target Sum](https://leetcode.com/problems/target-sum/) (Medium)
- LC 97: [Interleaving String](https://leetcode.com/problems/interleaving-string/) (Medium)
- LC 329: [Longest Increasing Path In a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) (Hard)
- LC 115: [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) (Hard)
- LC 72: [Edit Distance](https://leetcode.com/problems/edit-distance/) (Medium)
- LC 312: [Burst Balloons](https://leetcode.com/problems/burst-balloons/) (Hard)
- LC 10: [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) (Hard)

## Real-world applications
Sequence alignment and diff tools.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
dp = [[0]*(n+1) for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if a[i-1] == b[j-1]: dp[i][j] = 1+dp[i-1][j-1]
        else: dp[i][j] = max(dp[i-1][j],dp[i][j-1])
```

Complexity: O(m*n) time and space.


See [personal mistakes](mistakes.md) and [progress](problems.md).
