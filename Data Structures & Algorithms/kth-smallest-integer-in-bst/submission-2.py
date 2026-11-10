# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root

        while curr or stack:

            # Step 1: Keep going left
            while curr:
                stack.append(curr)
                curr = curr.left

            # Step 2: Pop the next smallest node
            curr = stack.pop()

            # Step 3: Decrease k
            k-=1

            # Step 4: If k == 0, return the answer
            if k == 0:
                return curr.val
            
            # Step 5: Move to the right subtree
            curr = curr.right