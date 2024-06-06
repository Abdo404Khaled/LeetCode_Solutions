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

        heap = list(m.keys())
        heapify(heap)

        while heap:
            x = heap[0]
            for i in range(x, x + groupSize):
                if i not in m:
                    return False
                m[i] -= 1
                if m[i] == 0:
                    if i != heap[0]:
                        return False
                    heappop(heap)
        return True

                    