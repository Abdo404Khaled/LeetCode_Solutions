class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        r = len(text1) + 1
        c = len(text2) + 1
        dp = [[0] * c for _ in range(r)]

        for i in range(r - 2, -1, -1):
            for j in range(c - 2, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
