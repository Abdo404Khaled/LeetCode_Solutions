class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        res = 0

        happiness.sort(reverse=True)

        for i in range(k):
            c = max(happiness[i] - i, 0)
            res += c
        
        return res