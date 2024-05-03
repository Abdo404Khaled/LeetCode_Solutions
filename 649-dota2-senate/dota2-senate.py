class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)

        qR = deque()
        qD = deque()

        for i, s in enumerate(senate):
            if s == 'R':
                qR.append(i)
            else:
                qD.append(i)

        while qR and qD:
            node1 = qR.popleft()
            node2 = qD.popleft()
            if node1 < node2:
                qR.append(n + node1)
            else:
                qD.append(n + node2)
        
        return 'Radiant' if qR else 'Dire'
        