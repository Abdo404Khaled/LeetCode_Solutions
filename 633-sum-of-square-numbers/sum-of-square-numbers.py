class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l, r = 0, int(sqrt(c))

        while l <= r:
            summation = l**2 + r**2
            if summation == c:
                return True
            elif summation > c:
                r -= 1
            else:
                l += 1
        
        return False

        