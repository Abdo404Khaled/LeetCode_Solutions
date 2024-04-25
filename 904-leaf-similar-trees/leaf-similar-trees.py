# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaves(root, temp):
            if not root:
                return
            if not root.right and not root.left:
                temp.append(root.val)
                return temp

            get_leaves(root.left, temp)
            get_leaves(root.right, temp)

            return temp
        
        return get_leaves(root1, []) == get_leaves(root2, [])

        