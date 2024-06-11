class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        numCounter = Counter(arr1)
        res = []
        for num in arr2:
            res.extend([num] * numCounter[num])
            del numCounter[num]
        
        res2 = []
        for num, freq in numCounter.items():
            res2.extend([num] * numCounter[num])
        
        res2.sort()
        return res + res2
        