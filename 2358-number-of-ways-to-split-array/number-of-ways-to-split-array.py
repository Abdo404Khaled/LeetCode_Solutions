class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
            suffix[n - i - 1] = suffix[n - i] + nums[n - i - 1]

        result = 0
        for i in range(len(nums) - 1):
            if prefix[i] >= suffix[i + 1]:
                result += 1
        
        return result