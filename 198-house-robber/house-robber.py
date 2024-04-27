class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        dp = nums[:]
        res = max(dp[0], dp[1])

        for i in range(2, n):
            S = [dp[j] for j in range(i - 1)]
            dp[i] = dp[i] + max(S)
            res = max(res, dp[i])
        return res
        