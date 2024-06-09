class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        increment = 1
        res = 0

        for _ in range(k):
            res += increment

            if res == 0 or res == n - 1:
                increment *= -1
        
        return res