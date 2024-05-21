class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(nums)
        l =[1]
        ans = []
        _sum = 1
        
        for i in range(n-1):
            if nums[i]%2==nums[i+1]%2:
                _sum += 0
            else:
                _sum += 1
            l.append(_sum)
        
        for q in queries:
            dist = abs(q[0]-q[1])
            if dist != l[q[1]] - l[q[0]]:
                ans.append(False)
            else:
                ans.append(True)
        return ans