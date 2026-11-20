# Backtracking — Interview patterns

## Recognition
Enumerate combinations, permutations or assignments

## Decision rules
Choose, recurse, undo; use start index for combinations and used set for permutations.

## Python reference: subsets

```python
def subsets(nums):
    result, path = [], []
    def dfs(i):
        if i == len(nums):
            result.append(path.copy())
            return
        dfs(i + 1)
        path.append(nums[i])
        dfs(i + 1)
        path.pop()
    dfs(0)
    return result
```

O(n*2^n) time including output; O(n) auxiliary stack.

## Common pitfalls
Copy mutable paths; skip duplicates at the same depth when necessary.

## Representative problems
- LC 78: [Subsets](https://leetcode.com/problems/subsets/) (Medium)
- LC 39: [Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium)
- LC 46: [Permutations](https://leetcode.com/problems/permutations/) (Medium)
- LC 90: [Subsets II](https://leetcode.com/problems/subsets-ii/) (Medium)
- LC 40: [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) (Medium)
- LC 79: [Word Search](https://leetcode.com/problems/word-search/) (Medium)
- LC 131: [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) (Medium)
- LC 17: [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) (Medium)
- LC 51: [N Queens](https://leetcode.com/problems/n-queens/) (Hard)

## Real-world applications
Constraint search and configuration enumeration.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
ans, path = [], []
def dfs(start):
    ans.append(path.copy())
    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(i+1)
        path.pop()
dfs(0)
```

Complexity: O(n*2^n) output time, O(n) recursion excluding output.


See [personal mistakes](mistakes.md) and [progress](problems.md).
