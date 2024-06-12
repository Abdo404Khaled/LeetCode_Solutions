class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for num in nums:
            count[num] += 1
        
        j = 0 
        
        for i, cnt in enumerate(count):
            for _ in range(cnt):
                nums[j] = i
                j += 1
        