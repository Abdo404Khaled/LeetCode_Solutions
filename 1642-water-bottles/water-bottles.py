class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        res = numBottles
        
        while numBottles >= numExchange:
            new = numBottles // numExchange
            rem = numBottles % numExchange
            res += new
            numBottles = new + rem
        
        return res
        