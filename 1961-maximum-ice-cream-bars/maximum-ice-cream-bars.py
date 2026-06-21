class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()

        n = len(costs)
        pre_sum = [0 for c in range(n)]

        pre_sum[0] = costs[0]

        if pre_sum[0] > coins:
            return 0

        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + costs[i]

            if pre_sum[i] > coins:
                return i
            elif pre_sum[i] == coins:
                return i + 1

        return n