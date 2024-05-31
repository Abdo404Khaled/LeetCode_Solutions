class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = defaultdict(int)
        res = []
        
        for n in nums:
            m[n] += 1
        
        for a, b in m.items():
            if b <= 1:
                res.append(a)
        
        return res
        