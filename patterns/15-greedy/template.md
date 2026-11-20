# Greedy — Interview patterns

## Recognition
Local choice, reachability, interval scheduling

## Decision rules
Use greedy only with an invariant or exchange proof; otherwise consider DP.

## Python reference: can_jump

```python
def can_jump(nums):
    far = 0
    for i, x in enumerate(nums):
        if i > far:
            return False
        far = max(far, i + x)
    return True
```

O(n) time, O(1) space.

## Common pitfalls
A locally largest value is not universally optimal; prove dominance.

## Representative problems
- LC 53: [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Medium)
- LC 55: [Jump Game](https://leetcode.com/problems/jump-game/) (Medium)
- LC 45: [Jump Game II](https://leetcode.com/problems/jump-game-ii/) (Medium)
- LC 134: [Gas Station](https://leetcode.com/problems/gas-station/) (Medium)
- LC 846: [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) (Medium)
- LC 1899: [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) (Medium)
- LC 763: [Partition Labels](https://leetcode.com/problems/partition-labels/) (Medium)
- LC 678: [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) (Medium)

## Real-world applications
Scheduling and routing heuristics.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
reach = 0
for i, x in enumerate(nums):
    if i > reach: return False
    reach = max(reach, i+x)
return True
```

Complexity: O(n) time, O(1) space.


See [personal mistakes](mistakes.md) and [progress](problems.md).
