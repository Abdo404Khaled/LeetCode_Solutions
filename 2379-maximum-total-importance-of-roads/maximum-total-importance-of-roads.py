class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        deg = [0] * n
        for e in roads:
            deg[e[0]] += 1
            deg[e[1]] += 1
        
        deg.sort()
        ans = 0
        for i in range(n):
            ans += (i + 1) * deg[i]
        
        return ans   