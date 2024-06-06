class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize:
            return False

        m = Counter(hand)

        while m:
            x = min(m)
            for i in range(x, x + groupSize):
                if i not in m:
                    return False
                m[i] -= 1
                if m[i] == 0:
                    del m[i]
        return True

                    