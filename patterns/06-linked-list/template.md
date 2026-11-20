# Linked List — Interview patterns

## Recognition
Pointer rewiring, cycle detection, nth from end, merge sorted streams.

## Decision rules
Use dummy head for deletion/merge; fast/slow for midpoint or cycle; save next before reversing.

## Python reference: reverse_list

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

O(n) time, O(1) auxiliary space.

## Common pitfalls
Guard fast and fast.next. Reorder: split first, reverse second, weave. Copy random pointer requires identity mapping, not values.

## Representative problems
- LC 206: [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy)
- LC 21: [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) (Easy)
- LC 143: [Reorder List](https://leetcode.com/problems/reorder-list/) (Medium)
- LC 19: [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium)
- LC 138: [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) (Medium)
- LC 2: [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (Medium)
- LC 141: [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) (Easy)
- LC 287: [Find The Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (Medium)
- LC 146: [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium)
- LC 23: [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) (Hard)
- LC 25: [Reverse Nodes In K Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (Hard)

## Real-world applications
Cache eviction chains and intrusive queues.

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev, cur = cur, nxt
return prev
```

Complexity: O(n) time, O(1) space.


See [personal mistakes](mistakes.md) and [progress](problems.md). Examples are reference solutions, not personal submissions.
