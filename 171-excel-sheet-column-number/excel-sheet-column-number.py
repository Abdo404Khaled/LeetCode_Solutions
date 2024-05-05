class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        res = 0
        n = len(columnTitle)
        
        for i in range(len(columnTitle)):
            weight = ord(columnTitle[n - i - 1]) - ord('A') + 1
            res += weight * 26 ** i
        
        return res