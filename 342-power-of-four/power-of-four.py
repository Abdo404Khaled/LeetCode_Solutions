class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        logvalue=log10(n)/log10(4)
        return logvalue==int(logvalue)