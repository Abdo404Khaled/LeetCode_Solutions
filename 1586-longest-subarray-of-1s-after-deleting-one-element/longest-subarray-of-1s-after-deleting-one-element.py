class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = prev = curr = 0

        for bit in nums:
            if bit:
                curr += 1
                longest = max(longest, prev + curr)
            else:
                prev, curr = curr, 0

        return longest - (longest == len(nums))