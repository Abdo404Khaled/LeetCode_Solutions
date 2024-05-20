class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return not (sqrt(num) - int(sqrt(num)))
        