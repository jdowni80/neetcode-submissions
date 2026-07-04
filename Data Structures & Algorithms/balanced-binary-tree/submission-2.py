# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            return 1 + max(height(root.left), height(root.right))
        
        curr_balanced = abs(height(root.left) - height(root.right)) < 2

        return curr_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)
        