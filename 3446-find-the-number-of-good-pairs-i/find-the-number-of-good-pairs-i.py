class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        n, m = len(nums1), len(nums2)
        for i in range(n):
            for j in range(m):
                if not nums1[i] % (nums2[j] * k):
                    res += 1
        
        return res