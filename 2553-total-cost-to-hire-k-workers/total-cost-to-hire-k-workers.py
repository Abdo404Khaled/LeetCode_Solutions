class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        left_heap, right_heap =costs[:candidates], costs[max(candidates,len(costs)-candidates):]

        heapify(left_heap)
        heapify(right_heap)

        res=0

        i=candidates
        j=len(costs)-candidates-1

        for _  in range(k):
            if not right_heap or (left_heap and right_heap[0] >= left_heap[0]):
                res += heappop(left_heap)
                if i <= j:
                    heappush(left_heap, costs[i])
                    i += 1
            else:
                res += heappop(right_heap)
                if i <= j:
                    heappush(right_heap, costs[j])
                    j -= 1
        
        return res
        

