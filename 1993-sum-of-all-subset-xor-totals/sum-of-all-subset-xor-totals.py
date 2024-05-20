class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        def helper(x, current):
            if x == len(nums):
                return current

            include = helper(x + 1, current ^ nums[x])
            exclude = helper(x + 1, current)
            
            return include + exclude
        
        
        return helper(0, 0)
            
                