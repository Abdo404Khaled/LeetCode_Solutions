class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i, res = 0, 0

        for j in range(len(nums)):
            if not nums[j]: k -= 1

            while k < 0:
                if not nums[i]: k += 1
                i += 1
            
            res = max(res, j - i + 1)
        
        return res
        