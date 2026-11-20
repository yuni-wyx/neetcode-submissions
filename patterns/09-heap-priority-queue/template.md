# Heap / Priority Queue: Heap; bounded top K

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
import heapq
heap = []
for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k: heapq.heappop(heap)
```

Complexity: O(n log(k+1)) time, O(k) space.
