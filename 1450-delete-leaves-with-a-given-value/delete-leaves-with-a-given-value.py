# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root:
            return None
        elif not root.left and not root.right:
            return None if root.val == target else root
        else:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
        
        if not root.left and not root.right:
            return self.removeLeafNodes(root, target)
        else:
            return root
        