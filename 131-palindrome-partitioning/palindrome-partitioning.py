class Solution(object):
    def compute_palindromes(self, s, dp):
        n = len(s)
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n: dp[i][i + 1] = (s[i] == s[i + 1])
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = (s[i] == s[j] and dp[i + 1][j - 1])
    
    def backtrack(self, index, s, curr, result, dp):
        if index >= len(s):
            result.append(list(curr))
            return
        for i in range(index, len(s)):
            if dp[index][i]:
                curr.append(s[index:i + 1])
                self.backtrack(i + 1, s, curr, result, dp)
                curr.pop()

    def partition(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        self.compute_palindromes(s, dp)
        result = []
        self.backtrack(0, s, [], result, dp)
        return result
        