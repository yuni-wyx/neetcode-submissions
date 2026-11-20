# Two Pointers — Interview patterns

## Recognition
Sorted pair search, palindrome, opposite ends, in-place compaction.

## Decision rules
If sorted, eliminate one endpoint using the sum; for unsorted pair search use hashing.

## Python reference: pair_sorted

```python
def pair_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        total = nums[l] + nums[r]
        if total == target:
            return [l, r]
        if total < target:
            l += 1
        else:
            r -= 1
    return []
```

O(n) time, O(1) auxiliary space.

## Common pitfalls
Three Sum needs sorting and duplicate skipping; container water moves the shorter side; do not apply sorted elimination to unsorted input.

## Representative problems
- LC 125: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (Easy)
- LC 167: [Two Sum II Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (Medium)
- LC 15: [3Sum](https://leetcode.com/problems/3sum/) (Medium)
- LC 11: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Medium)
- LC 42: [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard)

## Real-world applications
Matching sorted timestamp streams and in-place filtering.

## Additional original snippets

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


See [personal mistakes](mistakes.md) and [progress](problems.md). Examples are reference solutions, not personal submissions.
