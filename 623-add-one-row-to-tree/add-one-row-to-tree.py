# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            return TreeNode(val=val, left=root)

        def dfs(root, d):
            if not root:
                return
            if d == depth - 1:
                root.left = TreeNode(val=val, left=root.left)
                root.right = TreeNode(val=val, right=root.right)
            else:
                dfs(root.left, d + 1)
                dfs(root.right, d + 1)
        
        dfs(root, 1)
        return root