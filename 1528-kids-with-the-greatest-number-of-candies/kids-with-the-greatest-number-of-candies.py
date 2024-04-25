class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        n = len(candies)
        result = [False]*n

        for i in range(n):
            result[i] = True if candies[i] + extraCandies >= max_candies else False

        return result 