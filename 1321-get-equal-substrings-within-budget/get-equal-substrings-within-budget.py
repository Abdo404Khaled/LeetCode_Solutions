class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        l = curr = res = 0
        for r in range(len(s)):
            curr += abs(ord(s[r]) - ord(t[r]))
            if curr > maxCost:
                curr -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, r - l + 1)
        return res
        