# Math & Geometry: Matrix boundaries; coordinate transforms

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
