class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = defaultdict(int)
        for x in s:
            m[x] += 1
        
        res, carry = 0, 0
        for val in m.values():
            res += val//2
            if val == 1 or val%2 >= 1:
                carry = 1

        return res * 2 + carry
        