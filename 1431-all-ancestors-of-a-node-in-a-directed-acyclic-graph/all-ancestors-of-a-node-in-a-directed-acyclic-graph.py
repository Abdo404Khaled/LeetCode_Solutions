class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for a,b in edges:
            graph[b].append(a)
        
        cache = {}
        def dfs(node):
            if node in cache:
                return cache[node]

            res = set()
            for nei in graph[node]:
                res|=dfs(nei)
                res.add(nei)
            
            cache[node] = res
            return cache[node]

        res = []
        for i in range(n):
            res.append(sorted(dfs(i)))

        return res