# Sliding Window — Interview patterns

## Recognition
Contiguous substring/subarray; longest valid or shortest covering segment; fixed-size window.

## Decision rules
Expand right, restore invariant by moving left; update maximum after validity, minimum while valid.

## Python reference: longest_unique

```python
def longest_unique(s):
    last = {}
    left = best = 0
    for right, ch in enumerate(s):
        left = max(left, last.get(ch, -1) + 1)
        last[ch] = right
        best = max(best, right - left + 1)
    return best
```

O(n) time, O(k) space for k distinct characters.

## Common pitfalls
Never move left backward. Negative numbers can break sum-based monotonic windows. Sliding Window Maximum requires a monotonic deque, not a single maximum variable.

## Representative problems
- LC 121: [Best Time to Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (Easy)
- LC 3: [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium)
- LC 424: [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) (Medium)
- LC 567: [Permutation In String](https://leetcode.com/problems/permutation-in-string/) (Medium)
- LC 76: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard)
- LC 239: [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Hard)

## Real-world applications
Rolling telemetry, rate limits and streaming analytics.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
l = 0
counts = {}
best = 0
for r, x in enumerate(s):
    counts[x] = counts.get(x, 0) + 1
    while counts[x] > 1:
        counts[s[l]] -= 1
        l += 1
    best = max(best, r-l+1)
```

Complexity: O(n) time, O(k) space for distinct symbols.


See [personal mistakes](mistakes.md) and [progress](problems.md). Examples are reference solutions, not personal submissions.
