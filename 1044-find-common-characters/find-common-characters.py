class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common_count = Counter(words[0])
        
        for word in words[1:]:
            word_count = Counter(word)
            for char in common_count.keys():
                common_count[char] = min(common_count[char], word_count[char])
        
        res = []
        for char, count in common_count.items():
            res.extend([char] * count)
        
        return res
        