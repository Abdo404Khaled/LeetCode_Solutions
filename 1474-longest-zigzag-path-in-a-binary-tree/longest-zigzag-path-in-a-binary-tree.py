# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global max_val
        max_val = 0
        def dfs(root, nextDirection, depth):
            global max_val
            if not root:
                return
            elif nextDirection == 'l':
                dfs(root.left, 'r', depth + 1)
                dfs(root.right, 'l', 1)
            elif nextDirection == 'r':
                dfs(root.right, 'l', depth + 1)
                dfs(root.left, 'r', 1)
            max_val = max(max_val, depth)

        dfs(root.right, 'l', 1)
        dfs(root.left, 'r', 1)
        return max_val

        