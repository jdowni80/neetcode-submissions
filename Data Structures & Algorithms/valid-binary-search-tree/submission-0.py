# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True
            valid = lower < node.val < upper
            minimum = node.val
            maximum = node.val
            return valid and dfs(node.left, lower, maximum) and dfs(node.right, minimum, upper)

        return dfs(root, float("-inf"), float("inf"))

        
        