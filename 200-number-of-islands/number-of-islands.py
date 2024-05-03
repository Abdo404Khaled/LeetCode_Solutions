class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        result = 0

        def searchAdj(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            searchAdj(i + 1, j)
            searchAdj(i - 1, j)
            searchAdj(i, j + 1)
            searchAdj(i, j - 1)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    searchAdj(i, j)
                    result += 1
        
        return result
        