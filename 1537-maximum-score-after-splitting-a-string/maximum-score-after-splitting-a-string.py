class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = 0
        zeros, ones = 0, 0

        for i in range(n - 1, -1, -1):
            ones += int(s[i])
        
        for i in range(n - 1):
            zeros += 1 if not int(s[i]) else 0
            ones -= 1 if int(s[i]) else 0
            result = max(result, zeros + ones)

        return result

