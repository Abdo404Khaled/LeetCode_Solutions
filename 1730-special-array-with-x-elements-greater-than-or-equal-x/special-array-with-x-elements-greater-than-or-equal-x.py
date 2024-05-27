class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in range(len(nums) + 1):
            temp = 0
            for j in range(len(nums)):
                if nums[j] >= n:
                    temp += 1
            if temp == n:
                return n
        
        return -1