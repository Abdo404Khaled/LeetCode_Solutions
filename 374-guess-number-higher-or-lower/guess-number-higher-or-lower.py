# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n

        while low <= high:
            mid = (low + high) // 2
            guess_result = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result == -1:
                high = mid - 1
            else:
                low = mid + 1

        return -1
        