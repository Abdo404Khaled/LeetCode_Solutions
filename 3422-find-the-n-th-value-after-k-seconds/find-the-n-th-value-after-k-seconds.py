class Solution(object):
    def valueAfterKSeconds(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        def prefix(arr):
            for i in range(1, len(arr)):
                arr[i] = arr[i] + arr[i - 1]
            return arr
        
        arr = [1 for _ in range(n)]

        for _ in range(k):
            arr = prefix(arr)
        
        return arr[-1] % MOD

        