class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp = [cost[0], cost[1]] * n
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1], dp[i-2]) + (cost[i] if i < n else 0)
        
        return dp[n]