# 1-D Dynamic Programming — Interview patterns

## Recognition
Optimal/counting result over prefixes or positions

## Decision rules
Define state and transition; use rolling variables only when dependencies permit.

## Python reference: rob

```python
def rob(nums):
    prev2 = prev1 = 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
```

O(n) time, O(1) space.

## Common pitfalls
Distinguish counting from optimization; initialize impossible states correctly.

## Representative problems
- LC 70: [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (Easy)
- LC 746: [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) (Easy)
- LC 198: [House Robber](https://leetcode.com/problems/house-robber/) (Medium)
- LC 213: [House Robber II](https://leetcode.com/problems/house-robber-ii/) (Medium)
- LC 5: [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) (Medium)
- LC 647: [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) (Medium)
- LC 91: [Decode Ways](https://leetcode.com/problems/decode-ways/) (Medium)
- LC 322: [Coin Change](https://leetcode.com/problems/coin-change/) (Medium)
- LC 152: [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) (Medium)
- LC 139: [Word Break](https://leetcode.com/problems/word-break/) (Medium)
- LC 300: [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) (Medium)
- LC 416: [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) (Medium)

## Real-world applications
Sequential resource allocation.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
dp = [0]*(n+1)
dp[0] = 1
for i in range(1,n+1):
    dp[i] = dp[i-1]
    if i >= 2: dp[i] += dp[i-2]
```

Complexity: O(n) time, O(n) space; rolling variables possible.


See [personal mistakes](mistakes.md) and [progress](problems.md).
