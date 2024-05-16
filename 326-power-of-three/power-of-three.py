class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        logvalue=log10(n)/log10(3)
        return logvalue==int(logvalue)
        