# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            self.res += abs(l) + abs(r)

            return root.val + l + r - 1

        dfs(root)
        return self.res     