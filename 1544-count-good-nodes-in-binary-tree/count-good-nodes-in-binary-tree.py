# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, max_val):
            if not root:
                return 0
            count = 1 if root.val >= max_val else 0
            max_val = max(max_val, root.val)
            return dfs(root.left, max_val) + dfs(root.right, max_val) + count

        
        return dfs(root, -float('inf'))
        