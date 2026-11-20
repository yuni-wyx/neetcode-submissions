# Binary Search — Interview patterns

## Recognition
Sorted data or a monotonic yes/no feasibility predicate.

## Decision rules
Exact lookup uses inclusive bounds; minimum feasible answer uses lower-bound convergence.

## Python reference: min_feasible

```python
def min_feasible(lo, hi, feasible):
    # Preconditions: lo <= hi; hi is feasible; predicate is monotone.
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

O(log(range) * C) time for predicate cost C; O(1) auxiliary space excluding predicate.

## Common pitfalls
Koko uses ceiling division. Matrix flat indexing uses divmod(mid, cols). Rotated search must identify the sorted half; duplicates can change complexity.

## Representative problems
- LC 704: [Binary Search](https://leetcode.com/problems/binary-search/) (Easy)
- LC 74: [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) (Medium)
- LC 875: [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) (Medium)
- LC 153: [Find Minimum In Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) (Medium)
- LC 33: [Search In Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium)
- LC 981: [Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/) (Medium)
- LC 4: [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) (Hard)

## Real-world applications
Capacity planning and minimum resource allocation.

## Additional original snippets

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


See [personal mistakes](mistakes.md) and [progress](problems.md). Examples are reference solutions, not personal submissions.
