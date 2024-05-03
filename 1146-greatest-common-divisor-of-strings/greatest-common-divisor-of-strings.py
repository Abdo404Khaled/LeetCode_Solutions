class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(n1, n2):
            if not n2:
                return abs(n1)
            else:
                return gcd(n2, n1 % n2)

        if str1 + str2 != str2 + str1:
            return ""

        ans = gcd(len(str1), len(str2))

        return str1[:ans]