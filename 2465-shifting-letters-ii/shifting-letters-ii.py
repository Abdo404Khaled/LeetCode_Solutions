class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        delta = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction:
                delta[start] += 1
                delta[end + 1] -= 1
            else:
                delta[start] -= 1
                delta[end + 1] += 1
        
        for i in range(1, len(delta)):
            delta[i] += delta[i - 1]
        
        result = []
        orda = ord('a')
        for i, c in enumerate(s):
            current = (ord(c) - orda + delta[i]) % 26
            result.append(chr(current + orda))
        
        return ''.join(result)