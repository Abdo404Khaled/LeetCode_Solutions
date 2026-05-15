class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map_n = {}

        for i in nums:
            map_n[i] = map_n.get(i, 0) + 1
        
        res = (-1, -1)
        for i, x in map_n.items():
            if x > res[1]:
                res = (i, x)
        
        return res[0]
