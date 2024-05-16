# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.val == 2:
            return self.evaluateTree(root.right) or self.evaluateTree(root.left)
        elif root.val == 3:
            return self.evaluateTree(root.right) and self.evaluateTree(root.left)
        else:
            return root.val if root else 0
        
        