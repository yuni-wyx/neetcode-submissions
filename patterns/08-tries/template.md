# Tries — Interview patterns

## Recognition
Prefix search or dictionary words

## Decision rules
Trie for shared prefixes; DFS with trie pruning for board search.

## Python reference: trie

```python
class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[None] = True
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return None in node
```

O(L) per operation; O(total characters) storage.

## Common pitfalls
Prefix is not necessarily a complete word. Wildcards require branching.

## Representative problems
- LC 208: [Implement Trie Prefix Tree](https://leetcode.com/problems/implement-trie-prefix-tree/) (Medium)
- LC 211: [Design Add And Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) (Medium)
- LC 212: [Word Search II](https://leetcode.com/problems/word-search-ii/) (Hard)

## Real-world applications
Autocomplete and routing prefixes.

## Additional original snippets

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


See [personal mistakes](mistakes.md) and [progress](problems.md).
