class Solution(object):
    def addedInteger(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = 1
        min1, min2 = nums1[0], nums2[0]
        
        while i < len(nums1):
            min1 = min(min1, nums1[i])
            min2 = min(min2, nums2[i])
            i += 1

        return min2 - min1
        