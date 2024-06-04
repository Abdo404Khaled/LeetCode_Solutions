class Solution(object):
    def clearStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        heap = []

        for i, x in enumerate(s):
            if heap and x == "*":
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, (x, -i))
        
        ans = [''] * len(s)

        while heap:
            x, i = heappop(heap)
            ans[-i] = x
            
        return ''.join(ans)
        
        
        