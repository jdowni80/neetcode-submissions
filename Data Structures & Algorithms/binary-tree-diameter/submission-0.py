# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return depth
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        longestPath = self.maxDepth(root.left) + self.maxDepth(root.right)
        maxChildPath = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(maxChildPath, longestPath)

        