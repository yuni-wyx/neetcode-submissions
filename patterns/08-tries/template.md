# Tries: Prefix tree

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
trie = {}
for word in words:
    node = trie
    for ch in word:
        node = node.setdefault(ch, {})
    node[None] = True
```

Complexity: O(total characters) construction.
