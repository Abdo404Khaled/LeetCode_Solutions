class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)