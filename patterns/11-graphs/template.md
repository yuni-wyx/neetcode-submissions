# Graphs: Graph BFS/DFS; visited set

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
from collections import deque
q = deque([start])
seen = {start}
while q:
    u = q.popleft()
    for v in graph[u]:
        if v not in seen:
            seen.add(v)
            q.append(v)
```

Complexity: O(V+E) time, O(V) space.
