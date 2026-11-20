# Linked List: Pointer rewiring; fast/slow pointers

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
