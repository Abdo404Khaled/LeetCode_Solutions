class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
            
        start, end = -1, -1

        for i, n in enumerate(nums):
            if n == target:
                start = i
                break
        
        end = start
        while end < len(nums) and nums[end] == target:
            end += 1
        
        end = end - 1 if end != -1 else -1
        return [start, end]