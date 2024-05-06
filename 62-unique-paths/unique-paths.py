class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[m - 1][i] = 1
        
        for i in range(m):
            dp[i][n - 1] = 1
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        
        return dp[0][0]
        
        
        