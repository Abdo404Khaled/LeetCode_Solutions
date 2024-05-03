class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l1, l2 = len(str1), len(str2)

        def isDiv(l):
            if l1 % l or l2 % l:
                return False
            f1, f2 = l1 // l, l2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2
        
        for l in range(min(l1, l2), 0, -1):
            if isDiv(l):
                return str1[:l]
        return ""