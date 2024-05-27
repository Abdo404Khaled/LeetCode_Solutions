class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, res = 0, 0
        n = len(s)
        while i < n:
            Ls, Rs = 0, 0
            while i < n and (Ls != Rs or (not Ls and not Rs)):
                Ls += 1 if s[i] == 'L' else 0
                Rs += 1 if s[i] == 'R' else 0
                i += 1
            res += 1
        return res
        