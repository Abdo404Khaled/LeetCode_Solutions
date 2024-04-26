# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        max_val = -float('inf')
        max_index = -1
        level = 0

        q = deque()
        q.append(root)

        while q:
            temp = 0
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                temp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if temp > max_val:
                max_val = temp
                max_index = level

        return max_index