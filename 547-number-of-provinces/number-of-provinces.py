class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        res = 0

        def dfs(city):
            if city in visited:
                return 0
            else:
                visited.add(city)
                for i in range(len(isConnected[city])):
                    if i == city or not isConnected[city][i]:
                        continue
                    else:
                        dfs(i)
                return 1
        
        for i in range(len(isConnected)):
            res += dfs(i)
        return res        