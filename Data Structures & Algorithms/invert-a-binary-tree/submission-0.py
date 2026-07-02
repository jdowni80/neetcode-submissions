# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.right and not root.left:
            return root

        tempRight = root.right
        tempLeft = root.left
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)
        root.left = tempRight
        root.right = tempLeft
        
        return root

        
        