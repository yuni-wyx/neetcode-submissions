# Intervals — Interview patterns

## Recognition
Overlaps, merging, room allocation

## Decision rules
Sort starts to merge; sort ends for maximum nonoverlap; heap for active room ends.

## Python reference: merge

```python
def merge(intervals):
    out = []
    for start, end in sorted(intervals):
        if out and start <= out[-1][1]:
            out[-1][1] = max(out[-1][1], end)
        else:
            out.append([start, end])
    return out
```

O(n log n) time, O(n) space including sorted copy/output.

## Common pitfalls
Closed vs half-open endpoints change overlap tests.

## Representative problems
- LC 57: [Insert Interval](https://leetcode.com/problems/insert-interval/) (Medium)
- LC 56: [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium)
- LC 435: [Non Overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (Medium)
- LC 252: [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) (Easy)
- LC 253: [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) (Medium)
- LC 1851: [Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/) (Hard)

## Real-world applications
Calendar and reservation systems.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
merged = []
for a,b in sorted(intervals):
    if not merged or a > merged[-1][1]: merged.append([a,b])
    else: merged[-1][1] = max(merged[-1][1], b)
```

Complexity: O(n log n) time, O(n) output space.


See [personal mistakes](mistakes.md) and [progress](problems.md).
