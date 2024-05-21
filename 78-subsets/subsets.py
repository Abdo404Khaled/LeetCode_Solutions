class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        comp = []

        def backtrack(i):
            if  i >= len(nums):
                res.append(comp[:])
                return

            comp.append(nums[i])
            backtrack(i+1)
            comp.pop()
            
            backtrack(i+1)


        backtrack(0)
        return res

        