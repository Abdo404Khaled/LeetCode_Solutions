class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        res = 0

        happiness.sort(reverse=True)
        q = deque(happiness)

        for i in range(k):
            c = q.popleft() - i
            c = 0 if c <= 0 else c
            res += c
        
        return res