class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        res = r * 2**(c - 1)

        for j in range(1, c):
            cnt = 0
            for i in range(r):
                if grid[i][0] != grid[i][j]:
                    cnt += 1
            
            cnt = max(cnt, r - cnt)
            res += cnt * (2**(c - j - 1))

        return res
        