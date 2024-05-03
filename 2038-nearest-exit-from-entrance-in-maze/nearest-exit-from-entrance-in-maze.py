class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque([entrance])
        visited = set()
        res = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                    if maze[r][c] == '.' and [r, c] != entrance:
                        return res
                for mR, mC in dirs:
                    newR, newC = r + mR, c + mC
                    if (newR, newC) not in visited and 0 <= newR < m and 0 <= newC < n and maze[newR][newC] == '.':
                        visited.add((newR, newC))
                        q.append((newR, newC))
            res += 1
        return -1

        
        