class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n < 3:
            return False
        dig = '0123456789'
        uppr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower = 'abcdefghijklmnopqrstuvwxyz'
        vowels = 'aeiouAEIOU'
        cons = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        not_allowed = '@$#'
        has_v = False
        has_c = False
        has_d = False
        has_up = False
        has_lo = False
        for w in word:
            if w in not_allowed:
                return False
            if w in uppr:
                has_up = True
            if w in lower:
                has_lo = True
            if w in vowels:
                has_v = True
            if w in cons:
                has_c = True
            if w in dig:
                has_d = True
        return (has_v and has_c) and (has_d or has_up or has_lo)
        
                