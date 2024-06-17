class Solution(object):
    def minPatches(self, nums, target):
        i, res, upto = 0, 0, 0
        n = len(nums) 
        while upto < target:
            if i < n and nums[i] <= upto + 1:
                upto += nums[i]
                i += 1
            else:
                res += 1
                upto += upto + 1
        
        return res