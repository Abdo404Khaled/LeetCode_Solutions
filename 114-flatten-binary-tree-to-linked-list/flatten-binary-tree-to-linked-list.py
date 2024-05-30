# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node: 
                return
            if node.left:
                curr = node.left
                while curr.right:
                    curr = curr.right
                curr.right = node.right
                node.right = node.left
                node.left = None
            dfs(node.right)
        dfs(root)
        