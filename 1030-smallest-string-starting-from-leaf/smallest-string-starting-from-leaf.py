# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        self.smallest_string = ''
        self.helper(root, '')
        return self.smallest_string
    def helper(self, root, current_string):
        if root == None:
            return
        current_string = chr(root.val + ord('a')) + current_string
        if root.left == None and root.right == None:
            if self.smallest_string == '' or self.smallest_string>current_string:
                self.smallest_string = current_string
        if root.left:
            self.helper(root.left,current_string)
        if root.right:
            self.helper(root.right,current_string)