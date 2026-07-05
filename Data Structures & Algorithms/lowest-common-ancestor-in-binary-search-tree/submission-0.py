# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inTree(self, root: TreeNode, node: TreeNode) -> bool:
        if not root:
            return False
        return root.val == node.val or self.inTree(root.left, node) or self.inTree(root.right, node)
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        qInLeft = self.inTree(root.left, q)
        qInRight = self.inTree(root.right, q)
        pInLeft = self.inTree(root.left, p)
        pInRight = self.inTree(root.right, p)
        if pInLeft and qInRight:
            return root
        if pInRight and qInLeft:
            return root

        if p.val == root.val and self.inTree(root, q):
            return root
        if q.val == root.val and self.inTree(root, p):
            return root

        if qInLeft and pInLeft:
            return self.lowestCommonAncestor(root.left, p, q)
        if qInRight and pInRight:
            return self.lowestCommonAncestor(root.right, p, q)