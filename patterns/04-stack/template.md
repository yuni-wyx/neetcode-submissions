# Stack — Interview patterns

## Recognition
Nested delimiters, next greater element, undo, histogram boundaries.

## Decision rules
Use ordinary stack for nesting, monotonic stack of indices for unresolved next-greater queries.

## Python reference: daily_temperatures

```python
def daily_temperatures(nums):
    stack = []
    ans = [0] * len(nums)
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)
    return ans
```

O(n) amortized time, O(n) space.

## Common pitfalls
Check emptiness before pop. Strict versus non-strict comparison changes tie handling. RPN subtraction/division must preserve operand order.

## Representative problems
- LC 20: [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy)
- LC 155: [Min Stack](https://leetcode.com/problems/min-stack/) (Medium)
- LC 150: [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (Medium)
- LC 22: [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) (Medium)
- LC 739: [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (Medium)
- LC 853: [Car Fleet](https://leetcode.com/problems/car-fleet/) (Medium)
- LC 84: [Largest Rectangle In Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (Hard)

## Real-world applications
Parsing, undo history and threshold-event detection.

## Additional original snippets

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


See [personal mistakes](mistakes.md) and [progress](problems.md). Examples are reference solutions, not personal submissions.
