class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        memory = {}

        def recursion(i):
            if i == n - 1:
                return 0

            if i in memory:
                return memory[i]

            res = -1

            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    next_jumps = recursion(j)

                    if next_jumps != -1:
                        res = max(res, 1 + next_jumps)

            memory[i] = res
            return res

        return recursion(0)