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
        
        max_node = -1
        max_edge = -1

        for node in graph:
            if graph[node] > max_edge:
                max_node = node
                max_edge = graph[node]
        
        return max_node
