class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(int)

        for a,b in edges:
            graph[a] += 1
            graph[b] += 1
        
        nodes = len(graph) - 1

        for node in graph:
            if graph[node] == nodes:
                return node
        
        return 0
