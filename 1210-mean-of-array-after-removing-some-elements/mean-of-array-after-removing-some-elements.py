class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        return sum(sorted(arr)[int(0.05 * len(arr)): len(arr) - int(0.05 * len(arr))]) / float(len(arr) - 2 * int(0.05 * len(arr)))