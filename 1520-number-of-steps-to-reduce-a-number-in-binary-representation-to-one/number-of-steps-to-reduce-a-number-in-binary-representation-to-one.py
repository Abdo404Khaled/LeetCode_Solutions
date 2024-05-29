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
        # can you use bit manibulation to either shift right by 1 or add 1 after checking last bit
        res = 0
        while s != '1':
            if s[-1] == '0':
                s = s[:-1]
            else:
                s = bin(int(s, 2) + 1)[2:]
            res += 1
        
        return res
        return self.helper(int(s, 2))
        