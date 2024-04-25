# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def dfs(root, pathSum):
            if not root:
                return False
            if not root.left and not root.right:
                return (pathSum + root.val) == targetSum
            pathSum += root.val
            return dfs(root.left, pathSum) or dfs(root.right, pathSum)

        return dfs(root, 0)
