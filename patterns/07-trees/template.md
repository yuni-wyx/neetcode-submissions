# Trees: DFS / BFS; path state; Tree DP

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
def dfs(node):
    if node is None: return 0
    left = dfs(node.left)
    right = dfs(node.right)
    return 1 + max(left, right)
```

Complexity: O(n) time, O(h) stack.

## Tree DP: maximum path sum

```python
best = float('-inf')
def gain(node):
    nonlocal best
    if node is None: return 0
    l = max(0, gain(node.left))
    r = max(0, gain(node.right))
    best = max(best, node.val+l+r)
    return node.val+max(l,r)
```
Place inside an enclosing function; call gain(root), then return best. For diameter use heights and update best with l+r; return 1+max(l,r). O(n) time, O(h) stack.

## BFS levels

```python
from collections import deque
q = deque([root]) if root else deque()
levels = []
while q:
    level = []
    for _ in range(len(q)):
        node = q.popleft()
        level.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    levels.append(level)
```
O(n) time, O(w) queue excluding output.
