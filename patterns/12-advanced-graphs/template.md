# Advanced Graphs — Interview patterns

## Recognition
Weighted shortest paths, minimum spanning trees

## Decision rules
Dijkstra for nonnegative edges; Kruskal/Prim for MST; bounded-edge DP for flight constraints.

## Python reference: dijkstra

```python
import heapq
def dijkstra(graph, start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float('inf')):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist
```

O((V+E) log(V+E)) time, O(V+E) space for lazy heap; comparable node IDs assumed.

## Common pitfalls
No negative weights; discard stale heap entries; bounded stops require additional state.

## Representative problems
- LC 332: [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) (Hard)
- LC 1584: [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) (Medium)
- LC 743: [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium)
- LC 778: [Swim In Rising Water](https://leetcode.com/problems/swim-in-rising-water/) (Hard)
- LC 269: [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) (Hard)
- LC 787: [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) (Medium)

## Real-world applications
Network routing and weighted route planning.

## Additional original snippets

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


See [personal mistakes](mistakes.md) and [progress](problems.md).
