class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        
        first_word_chars = set(words[0])
        
        res = []
        
        for char in first_word_chars:
            min_count = min(word.count(char) for word in words)
            res.extend([char] * min_count)
        
        return res
        