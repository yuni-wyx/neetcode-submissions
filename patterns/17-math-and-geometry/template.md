# Math & Geometry — Interview patterns

## Recognition
Matrix coordinates, rotation, arithmetic simulation

## Decision rules
Track coordinate transforms and boundaries; use integer arithmetic when exactness matters.

## Python reference: rotate

```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```

O(n^2) time, O(1) auxiliary space for square matrix.

## Common pitfalls
Validate dimensions and mutation requirements; beware floating-point equality.

## Representative problems
- LC 48: [Rotate Image](https://leetcode.com/problems/rotate-image/) (Medium)
- LC 54: [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) (Medium)
- LC 73: [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) (Medium)
- LC 202: [Happy Number](https://leetcode.com/problems/happy-number/) (Easy)
- LC 66: [Plus One](https://leetcode.com/problems/plus-one/) (Easy)
- LC 50: [Pow(x, n)](https://leetcode.com/problems/powx-n/) (Medium)
- LC 43: [Multiply Strings](https://leetcode.com/problems/multiply-strings/) (Medium)
- LC 2013: [Detect Squares](https://leetcode.com/problems/detect-squares/) (Medium)

## Real-world applications
Image transforms and spatial grids.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
# Rotate square matrix clockwise
n = len(matrix)
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
for row in matrix: row.reverse()
```

Complexity: O(n^2) time, O(1) auxiliary space.


See [personal mistakes](mistakes.md) and [progress](problems.md).
