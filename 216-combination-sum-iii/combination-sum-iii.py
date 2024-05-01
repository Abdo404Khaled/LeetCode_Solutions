class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if not k:
            return []

        res = []
        def backtrack(path, start, k, target):
            if k == 0 and target == 0:
                res.append(path[:])
                return 
            
            if k == 0 or target <= 0:
                return
            
            for i in range(start,10):
                backtrack(path+[i], i+1, k-1, target-i)
            

        backtrack([], 1, k, n)
        return res
        