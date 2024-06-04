class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_chairs = 0
        available_chairs = 0

        for x in s:
            if x == "E":
                if available_chairs <= 0:
                    min_chairs += 1
                else:
                    available_chairs -= 1
            else:
                available_chairs += 1

        return min_chairs
        