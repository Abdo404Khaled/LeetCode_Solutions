class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        mapper = defaultdict()

        for i, char in enumerate(s):
            if char not in mapper:
                mapper[char] = [i, i]
            else:
                mapper[char][-1] = i
        
        for start, end in mapper.values():
            if start == end:
                continue
            
            seen = set()
            for i in range(start + 1, end):
                seen.add(s[i])
            result += len(seen)
        
        return result

        