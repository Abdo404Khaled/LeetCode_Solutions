class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        res = 0

        for i in range(n - 1):
            current = arr[i]
            for k in range(i + 1, n):
                current ^= arr[k]
                if current == 0:
                    res += (k - i)
        
        return res