class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l, r = 0, len(nums) - 1
        print(nums)
        while l < r:
            if -nums[l] == nums[r]:
                return nums[r]
            elif -nums[l] <= nums[r]:
                r -= 1
            else:
                l += 1
        return -1