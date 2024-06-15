class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapify(minCapital)

        for _ in range(k):

            while minCapital and minCapital[0][0] <= w:
                c, p = heappop(minCapital)
                heappush(maxProfit, -p)
            
            if not maxProfit:
                break
            
            w += -heappop(maxProfit)
        
        return w

        
        