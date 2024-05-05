class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = defaultdict(int)
        res = 0
        for n in nums:
            s[n] += 1
            res += n

        for n in s.keys():
            if s[n] > 1:
                res -= n * s[n]

        return res
        