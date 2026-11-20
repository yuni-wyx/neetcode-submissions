# Bit Manipulation: XOR; bit masks

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
ans = 0
for x in nums: ans ^= x
return ans
```

Complexity: O(n) time, O(1) auxiliary space (fixed-width integers).
