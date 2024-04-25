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
        :rtype: int
        """
        if not root:
            return 0
        
        nums = []

        global count 
        count = 0

        def dfs(root):
            if not root:
                return

            nums.append(root.val)
            dfs(root.left)
            dfs(root.right)

            global count
            temp = 0
            for i in range(len(nums) - 1, -1, -1):
                temp += nums[i]
                if temp == targetSum:
                    count += 1
            
            nums.pop()

        dfs(root)
        return count
        
        