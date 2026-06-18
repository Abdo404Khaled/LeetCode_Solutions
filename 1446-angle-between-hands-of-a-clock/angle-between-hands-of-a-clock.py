class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """

        current_h_hand = (minutes / 60.0) * 30.0
        between = hour * 30
        angle = abs((between + current_h_hand) - minutes * (360/60))

        return min(angle, 360 - angle)
