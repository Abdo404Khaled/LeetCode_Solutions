class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        
        for i in range(len(nums) - 1):
            if (not (nums[i] % 2) and nums[i + 1] % 2) or (nums[i] % 2 and not (nums[i + 1] % 2)):
                continue
            else:
                return False

        return True
        