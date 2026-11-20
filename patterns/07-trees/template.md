# Trees — Interview patterns

## Recognition
Recursive subtree properties, root-to-leaf state, breadth levels, BST ordering.

## Decision rules
Postorder for child results; preorder for inherited bounds/state; BFS for levels. Separate global answer from branch return.

## Python reference: tree_max_path

```python
def tree_max_path(root):
    best = float('-inf')
    def gain(node):
        nonlocal best
        if node is None:
            return 0
        l = max(0, gain(node.left))
        r = max(0, gain(node.right))
        best = max(best, node.val + l + r)
        return node.val + max(l, r)
    gain(root)
    return best
```

O(n) time, O(h) recursion space; assumes nonempty tree.

## Common pitfalls
LC124 global path uses both children but return only one. LC105 left inorder range ends at mid-1; index map avoids repeated search. BST validation needs ancestor bounds; good-node path maximum is branch-local.

## Representative problems
- LC 226: [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) (Easy)
- LC 104: [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) (Easy)
- LC 543: [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) (Easy)
- LC 110: [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) (Easy)
- LC 100: [Same Tree](https://leetcode.com/problems/same-tree/) (Easy)
- LC 572: [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) (Easy)
- LC 235: [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) (Medium)
- LC 102: [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (Medium)
- LC 199: [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) (Medium)
- LC 1448: [Count Good Nodes In Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) (Medium)
- LC 98: [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (Medium)
- LC 230: [Kth Smallest Element In a Bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (Medium)
- LC 105: [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (Medium)
- LC 124: [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (Hard)
- LC 297: [Serialize And Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (Hard)

## Real-world applications
Hierarchy aggregation, dependency trees and search planning (tree-shaped cases).

## Additional original snippets

Representative Python pattern (adapt inputs, invariants and return values to the problem; snippets are not standalone programs).

```python
def dfs(node):
    if node is None: return 0
    left = dfs(node.left)
    right = dfs(node.right)
    return 1 + max(left, right)
```

Complexity: O(n) time, O(h) stack.

## Tree DP: maximum path sum

```python
best = float('-inf')
def gain(node):
    nonlocal best
    if node is None: return 0
    l = max(0, gain(node.left))
    r = max(0, gain(node.right))
    best = max(best, node.val+l+r)
    return node.val+max(l,r)
```
Place inside an enclosing function; call gain(root), then return best. For diameter use heights and update best with l+r; return 1+max(l,r). O(n) time, O(h) stack.

## BFS levels

```python
from collections import deque
q = deque([root]) if root else deque()
levels = []
while q:
    level = []
    for _ in range(len(q)):
        node = q.popleft()
        level.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    levels.append(level)
```
O(n) time, O(w) queue excluding output.


See [personal mistakes](mistakes.md) and [progress](problems.md). Examples are reference solutions, not personal submissions.
