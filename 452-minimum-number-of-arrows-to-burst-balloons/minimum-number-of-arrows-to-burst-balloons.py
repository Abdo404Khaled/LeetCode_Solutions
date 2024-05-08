class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        res = len(points)
        start = -float('inf')
        for s, e in points:
            if s <= start:
                res -= 1
                start = min(start, e)
            else:
                start = e
        
        return res

        