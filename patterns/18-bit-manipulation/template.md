# Bit Manipulation — Interview patterns

## Recognition
XOR cancellation, masks, binary representation

## Decision rules
Use XOR for paired cancellation; x & (x-1) clears lowest set bit.

## Python reference: single_number

```python
def single_number(nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans
```

O(n) time, O(1) word space under fixed-width model.

## Common pitfalls
XOR cancellation assumes pairs; Python negative integers need explicit width masks for fixed-width bit tasks.

## Representative problems
- LC 136: [Single Number](https://leetcode.com/problems/single-number/) (Easy)
- LC 191: [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) (Easy)
- LC 338: [Counting Bits](https://leetcode.com/problems/counting-bits/) (Easy)
- LC 190: [Reverse Bits](https://leetcode.com/problems/reverse-bits/) (Easy)
- LC 268: [Missing Number](https://leetcode.com/problems/missing-number/) (Easy)
- LC 371: [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) (Medium)
- LC 7: [Reverse Integer](https://leetcode.com/problems/reverse-integer/) (Medium)

## Real-world applications
Flags, compact state and low-level protocols.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
ans = 0
for x in nums: ans ^= x
return ans
```

Complexity: O(n) time, O(1) auxiliary space (fixed-width integers).


See [personal mistakes](mistakes.md) and [progress](problems.md).
