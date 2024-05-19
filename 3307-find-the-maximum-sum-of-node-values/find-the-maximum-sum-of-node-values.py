class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        delta = [(n ^ k) - n for n in nums]
        delta.sort(reverse=True)
        res = sum(nums)

        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                break
            d = delta[i] + delta[i + 1]
            if d <= 0:
                break
            res += d
        
        return res

        