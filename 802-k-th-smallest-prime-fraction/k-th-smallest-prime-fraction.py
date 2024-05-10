class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, fractions = len(arr), []

        for i in range(n):
            for j in range(i, n):
                fractions.append([arr[i], arr[j]])

        fractions.sort(key = lambda x: float(x[0]) / float(x[1]))
        return fractions[k - 1]