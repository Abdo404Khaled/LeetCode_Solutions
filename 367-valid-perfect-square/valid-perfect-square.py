class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start, end = 1, num

        while start <= end:
            mid = start + (end - start) / 2

            if mid * mid == num: return True
            elif mid * mid > num: end = mid - 1
            else: start = mid + 1

        return False
        