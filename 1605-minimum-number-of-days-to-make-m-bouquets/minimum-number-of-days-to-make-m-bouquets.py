class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if(m*k>len(bloomDay)):return -1
        def isValid(val):
            counter,run=0,0
            for i in bloomDay:
                if(i<=val):run+=1
                else:
                    counter+=run//k
                    run=0
            counter+=run//k
            return counter>=m
        
        l=0
        r=max(bloomDay)
        while(l<r):
            mid=(l+r)//2
            if(isValid(mid)):r=mid
            else:l=mid+1
        return r  