class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        odd = 0
        
        for x in arr:
            if not x % 2:
                odd = 0
            else:
                odd += 1
            
            if odd == 3:
                return True
        
        return False