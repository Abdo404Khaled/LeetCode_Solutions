class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ''
        i, j = 0, 0
        n, m = len(word1), len(word2)
        
        while i < n and j < m:
            result += word1[i]
            result += word2[i]
            i += 1
            j += 1

        while i < n:
            result += word1[i]
            i += 1
        
        while j < m:
            result += word2[j]
            j += 1

        return result
        