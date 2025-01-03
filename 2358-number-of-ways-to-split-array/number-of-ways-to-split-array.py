class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        result = 0
        
        for i in range(n - 1):
            prefix_sum += nums[i]
            suffix_sum = total_sum - prefix_sum
            if prefix_sum >= suffix_sum:
                result += 1
        
        return result