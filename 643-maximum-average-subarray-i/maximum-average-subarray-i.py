class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxA = sum(nums[:k]) / float(k)
        res = maxA
        for i in range(len(nums) - k):
            maxA *= k
            maxA -= nums[i]
            maxA += nums[i + k]
            maxA = maxA / float(k)
            res = max(res, maxA)
        
        return res
        
        