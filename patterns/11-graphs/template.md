# Graphs — Interview patterns

## Recognition
Connectivity, shortest unweighted path, prerequisites

## Decision rules
BFS for shortest unweighted path; DFS for components; topological sort for DAG dependencies.

## Python reference: bfs

```python
from collections import deque
def distances(graph, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph.get(u, []):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
```

O(V+E) time, O(V) space.

## Common pitfalls
Mark visited at enqueue; directed cycles require recursion colors or indegrees.

## Representative problems
- LC 200: [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium)
- LC 133: [Clone Graph](https://leetcode.com/problems/clone-graph/) (Medium)
- LC 695: [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) (Medium)
- LC 417: [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (Medium)
- LC 130: [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) (Medium)
- LC 994: [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) (Medium)
- LC 286: [Walls And Gates](https://leetcode.com/problems/walls-and-gates/) (Medium)
- LC 207: [Course Schedule](https://leetcode.com/problems/course-schedule/) (Medium)
- LC 210: [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (Medium)
- LC 684: [Redundant Connection](https://leetcode.com/problems/redundant-connection/) (Medium)
- LC 323: [Number of Connected Components In An Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) (Medium)
- LC 261: [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) (Medium)
- LC 127: [Word Ladder](https://leetcode.com/problems/word-ladder/) (Hard)

## Real-world applications
Dependency graphs and robotic grid navigation.

## Additional original snippets

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


See [personal mistakes](mistakes.md) and [progress](problems.md).
