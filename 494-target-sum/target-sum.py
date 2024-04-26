class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.memo = {}

        def dfs(index, current_sum):
            if index == len(nums):
                if current_sum == target:
                    return 1
                return 0

            if (index, current_sum) in self.memo:
                return self.memo[(index, current_sum)]

            add = dfs(index + 1, current_sum + nums[index])
            subtract = dfs(index + 1, current_sum - nums[index])

            self.memo[(index, current_sum)] = add + subtract
            return self.memo[(index, current_sum)]

        return dfs(0, 0)
        