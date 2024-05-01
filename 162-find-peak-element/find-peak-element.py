class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low, high = 0, n-1
        while low <= high:
            mid = ((high-low)//2) + low
            if mid > 0 and nums[mid] < nums[mid-1]:
                high = mid-1
            elif mid < n-1 and nums[mid] < nums[mid+1]:
                low = mid+1  
            else:
                return mid