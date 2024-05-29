class Solution(object):
    def helper(self, s):
        if s == 1:
            return 0
        else:
            return 1 + self.helper(s / 2 if not s % 2 else s + 1)
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.helper(int(s, 2))
        