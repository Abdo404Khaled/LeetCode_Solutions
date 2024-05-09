class Solution(object):
    def countVowels(self, s):
        vowels = 'aeiou'

        res = 0
        for ch in s:
            res += 1 if ch in vowels else 0
        
        return res
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = 'aeiou'
        c = s[:k]
        res = self.countVowels(c)
        temp = res
        for i in range(1, len(s) - k + 1):
            temp -= 1 if c[0] in vowels else 0
            c = c[1:]
            c += s[i+k-1:i+k]
            temp += 1 if c[-1] in vowels else 0
            res = max(res, temp)
        
        return res

        
        

        