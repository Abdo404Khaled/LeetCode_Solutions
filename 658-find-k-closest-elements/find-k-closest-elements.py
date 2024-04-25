class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        return sorted(heapq.nsmallest(k, arr, key=lambda a: abs(a - x)))
        