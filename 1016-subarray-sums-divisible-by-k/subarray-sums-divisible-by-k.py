class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        current = 0

        remainder_map = defaultdict(int)
        remainder_map[0] = 1

        for n in nums:
            current += n
            remainder = current % k

            res += remainder_map[remainder]
            remainder_map[remainder] += 1
        
        return res