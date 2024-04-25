class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumMap = defaultdict(int)
        result = 0

        for i in range(len(nums)):
            val = k - nums[i]
            if val in sumMap:
                result += 1
                if sumMap[val] == 1: sumMap.pop(val)
                else: sumMap[val] -= 1
            else:
                sumMap[nums[i]] += 1
        
        return result