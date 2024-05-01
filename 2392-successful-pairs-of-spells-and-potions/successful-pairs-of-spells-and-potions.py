class Solution(object):
    def search(self, spell, arr, n, low, high, success):
        while low <= high:
            mid = low + (high - low) // 2
            product = spell * arr[mid]
            if product < success:
                low = mid + 1
            else:
                high = mid - 1
        
        return n - low

    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        n = len(potions)
        potions.sort()

        res = []
        memo = {}

        for spell in spells:
            if spell in memo:
                res.append(memo[spell])
                continue
            memo[spell] = self.search(spell, potions, n, 0, n - 1, success)
            res.append(memo[spell])
        
        return res
        
        