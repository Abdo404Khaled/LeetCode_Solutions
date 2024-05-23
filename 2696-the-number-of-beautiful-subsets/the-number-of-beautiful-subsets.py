class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def backtrack(i, n):
            if i >= len(nums):
                return 1

            res = backtrack(i + 1, n)

            if not n[nums[i] + k] and not n[nums[i] - k]:
                n[nums[i]] += 1
                res += backtrack(i + 1, n)
                n[nums[i]] -= 1
            
            return res
    
        return backtrack(0, defaultdict(int)) - 1