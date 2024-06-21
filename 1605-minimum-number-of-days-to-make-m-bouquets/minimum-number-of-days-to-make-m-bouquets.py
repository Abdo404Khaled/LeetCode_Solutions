class Solution(object):
    def canMake(self, needed_bouquets, needed_flowers, flowers, day):
        bouquets, adjacent = 0, 0
        for flower in flowers:
            if flower <= day:
                adjacent += 1
            else:
                bouquets += adjacent // needed_flowers
                adjacent = 0

        bouquets += adjacent // needed_flowers
        return bouquets >= needed_bouquets
        
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m*k > len(bloomDay):
            return -1
        
        l, r = 0, max(bloomDay)

        while l < r:
            mid = (l + r) // 2
            if self.canMake(m, k, bloomDay, mid):
                r = mid
            else:
                l = mid + 1
        
        return r
        
