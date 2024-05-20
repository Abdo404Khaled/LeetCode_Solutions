class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 2 == 0:
            return self.isUgly(n // 2)
        elif n % 3 == 0:
            return self.isUgly(n // 3)
        elif n % 5 == 0:
            return self.isUgly(n // 5)
        else:
            return False
        