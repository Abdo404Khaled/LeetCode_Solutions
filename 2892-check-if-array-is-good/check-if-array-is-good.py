class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # good if nums is permutation of based[n]
        # base[n] is n+1 array from 1 to n and n twice
        # base[3] [1, 2, 3, 3]

        # max = 4
        # {1: 1, 2: 1, 3: 1, 4: 2} True

        max_n = 1
        map_n = defaultdict(int)

        for num in nums:
            if num > max_n:
                max_n = num
            map_n[num] += 1

        for num in range(1, max_n):
            if num not in map_n:
                map_n[num] = 0

        for num, occ in map_n.items():
            if num == max_n and occ != 2:
                return False
            elif num != max_n and occ != 1:
                return False
        
        return True
