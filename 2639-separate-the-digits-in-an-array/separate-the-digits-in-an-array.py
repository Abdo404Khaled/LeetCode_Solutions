class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for num in nums:
            x = []
            while num:
                x.append(num % 10)
                num = num // 10
            res.extend(x[::-1])
        
        return res
            