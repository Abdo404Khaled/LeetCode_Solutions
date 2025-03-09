class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        count = 0
        left = 0

        for right in range(n + k - 1):
            index = right % n
            if colors[index] == colors[index - 1]:
                left = right

            if right - left + 1 >= k:
                count += 1

        return count