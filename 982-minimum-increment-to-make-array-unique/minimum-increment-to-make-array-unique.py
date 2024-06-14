class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1 [1] 2 2 3 7
        # 1 - 1 + 1 = 1
        # 1 2 2 2 3 7
        ###################
        # 1 2 [2] 2 3 7
        # 2 - 2 + 1 = 1
        # 1 2 3 2 3 7
        ###################
        # 1 2 3 [2] 3 7
        # 3 - 2 + 1 = 2
        # 1 2 3 4 3 7
        ###################
        # 1 2 3 4 [3] 7
        # 4 - 3 + 1 = 2
        # 1 2 3 4 5 7
        ###################
        # 1 2 3 4 5 7
        # res = 1 + 1 + 2 + 2= 6 #solved
        

        nums.sort()
        res = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                addition = nums[i - 1] - nums[i] + 1
                res += addition
                nums[i] += addition
            
        return res

                
                 
        