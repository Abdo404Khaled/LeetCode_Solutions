class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        stack = []
        
        for x in s:
            if x == "(":
                stack.append(x)
            elif x == ")":
                stack.pop()
            
            res = max(len(stack), res)
        
        return res
            
        