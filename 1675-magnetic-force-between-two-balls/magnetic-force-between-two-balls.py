class Solution(object):
    def check_good(self, force, positions, target):
        balls, previous_ball = 0, -self.INF

        for position in positions:
            if position - previous_ball >= force:
                balls += 1
                previous_ball = position
        
        return balls >= target


    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        self.INF = 10 ** 20
        position.sort()

        l, r = 1, position[-1] - position[0]

        while l < r:
            mid = (l + r + 1) // 2

            if self.check_good(mid, position, m):
                l = mid
            else:
                r = mid - 1
        
        return l