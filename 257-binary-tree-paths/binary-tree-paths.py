# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path + str(root.val))
                return
            dfs(root.left, path + str(root.val) + '->')
            dfs(root.right, path + str(root.val) + '->')
        
        dfs(root, "")
        return res
        