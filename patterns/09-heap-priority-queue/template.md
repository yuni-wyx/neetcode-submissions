# Heap / Priority Queue — Interview patterns

## Recognition
Top K, repeatedly smallest/largest, scheduling

## Decision rules
Fixed-size min heap for largest K; two heaps for running median.

## Python reference: top_k

```python
import heapq
def top_k(nums, k):
    if k <= 0:
        return []
    heap = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap
```

O(n log(k+1)) time, O(k) space; output unordered.

## Common pitfalls
Heap is not a sorted array; use tie-breakers for noncomparable payloads.

## Representative problems
- LC 703: [Kth Largest Element In a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) (Easy)
- LC 1046: [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (Easy)
- LC 973: [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) (Medium)
- LC 215: [Kth Largest Element In An Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium)
- LC 621: [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium)
- LC 355: [Design Twitter](https://leetcode.com/problems/design-twitter/) (Medium)
- LC 295: [Find Median From Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (Hard)

## Real-world applications
Priority scheduling and ranking.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
import heapq
heap = []
for x in nums:
    heapq.heappush(heap, x)
    if len(heap) > k: heapq.heappop(heap)
```

Complexity: O(n log(k+1)) time, O(k) space.


See [personal mistakes](mistakes.md) and [progress](problems.md).
