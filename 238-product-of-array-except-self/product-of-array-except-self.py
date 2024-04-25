class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        curr_right = 1
        curr_left = 1
        for i in range(n):
            res[i] *= curr_left
            curr_left *= nums[i]
            
            res[n - 1 - i] *= curr_right
            curr_right *= nums[n - 1 - i]
            
        return res