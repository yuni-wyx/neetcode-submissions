# Advanced Graphs: Dijkstra; MST; topological ordering

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
import heapq
dist = {start: 0}
heap = [(0, start)]
while heap:
    d, u = heapq.heappop(heap)
    if d != dist[u]: continue
    for v, w in graph[u]:
        nd = d+w
        if nd < dist.get(v, float('inf')):
            dist[v] = nd
            heapq.heappush(heap, (nd, v))
```

Complexity: O((V+E) log(V+E)) time with lazy heap; O(V+E) space.
