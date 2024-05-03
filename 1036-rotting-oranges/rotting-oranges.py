class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res, cntF = -1, 0
        q = deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i, j))
                if grid[i][j] == 1: cntF += 1
        
        if not cntF and not q: return 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                r, c = q.popleft() # rotten
                for dR, dC in dirs:
                    newR, newC = r + dR, c + dC
                    if 0 <= newR < m and 0 <= newC < n and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        cntF -= 1
                        q.append((newR, newC))
            res += 1

        return -1 if cntF else res
