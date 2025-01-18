class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        result = 0
        n, m = len(nums1), len(nums2)
        
        x1 = reduce(lambda a, b: a ^ b, nums1) if m % 2 != 0 else 0
        x2 = reduce(lambda a, b: a ^ b, nums2) if n % 2 != 0 else 0

        return x1 ^ x2
        