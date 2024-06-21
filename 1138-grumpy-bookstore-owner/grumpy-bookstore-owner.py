class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        l = 0
        r = minutes-1
        tot = sum(c for i,c in enumerate(customers) if grumpy[i]==0 and i>=minutes)
        
        diff = sum(customers[:minutes])
        tot += diff
        ans = tot
        while r<len(customers):
            
            if grumpy[l]==1:
                tot-=customers[l]
            l+=1
            r+=1
            if r<len(customers) and grumpy[r]==1:
                tot+=customers[r]
            ans = max(ans, tot)
        
        return ans