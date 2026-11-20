# Arrays & Hashing — Interview patterns

## Recognition
Use a set for existence, a dict for counts/index lookup, prefix/suffix for products without division.

## Decision rules
Complement lookup: store prior indices only; frequency map: key is item, value is count.

## Python reference: two_sum

```python
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```

O(n) expected time, O(n) space.

## Common pitfalls
Do not reuse the same index. For Top K, repeated max scans cost O(k*m) for m distinct keys; buckets or a heap avoid repeated scans. For encoding, reset the delimiter cursor per item and append only after parsing length.

## Representative problems
- LC 217: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (Easy)
- LC 242: [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (Easy)
- LC 1: [Two Sum](https://leetcode.com/problems/two-sum/) (Easy)
- LC 49: [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium)
- LC 347: [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium)
- LC 238: [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium)
- LC 36: [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) (Medium)
- LC 271: [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Medium)
- LC 128: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (Medium)

## Real-world applications
Deduplication, inventory counts and join-like lookup.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1
```

Complexity: O(n) time, O(n) space.


See [personal mistakes](mistakes.md) and [progress](problems.md). Examples are reference solutions, not personal submissions.
