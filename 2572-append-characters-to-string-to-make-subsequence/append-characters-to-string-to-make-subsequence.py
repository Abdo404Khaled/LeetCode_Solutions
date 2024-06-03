class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        nS = len(s)
        nT = len(t)
        pS = 0
        pT = 0

        while pS < nS and pT < nT:
            if s[pS] == t[pT]:
                pT += 1
            pS += 1
        return nT - pT