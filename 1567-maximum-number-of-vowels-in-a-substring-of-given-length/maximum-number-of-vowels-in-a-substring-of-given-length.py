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
        cnt = self.countVowels(c)
        res = cnt

        for i in range(len(s)-k):
            if s[i] in 'aeiou':
                cnt-=1
            if s[i+k] in 'aeiou':
                cnt+=1
            res = max(res, cnt)

        return res

        
        

        