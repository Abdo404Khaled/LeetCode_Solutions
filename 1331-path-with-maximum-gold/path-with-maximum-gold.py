class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0

            temp = grid[i][j]
            grid[i][j] = 0
            max_gold = temp + max(dfs(i + 1, j), dfs(i - 1, j), dfs(i, j + 1), dfs(i, j - 1))
            grid[i][j] = temp

            return max_gold
        
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    res = max(res, dfs(i, j))
        
        return res
