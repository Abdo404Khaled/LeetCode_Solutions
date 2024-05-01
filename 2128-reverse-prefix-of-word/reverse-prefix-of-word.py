class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        i = 0
        n = len(word)
        while i < n:
            if word[i] == ch:
                break
            i += 1
        
        return word[:i+1][::-1] + word[i+1:] if i < n else word
        