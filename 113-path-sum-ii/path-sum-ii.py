# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []

        def dfs(root, pathSum, temp):
            if not root:
                return
            if not root.left and not root.right:
                if (pathSum + root.val) == targetSum:
                    temp.append(root.val)
                    res.append(temp[:])
                    temp.pop()
                return 
            pathSum += root.val
            temp.append(root.val)
            dfs(root.left, pathSum, temp)
            dfs(root.right, pathSum, temp)
            temp.pop()

        dfs(root, 0, [])
        return res