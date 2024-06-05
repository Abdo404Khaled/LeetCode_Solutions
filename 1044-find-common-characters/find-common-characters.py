class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        
        n = len(words)
        m = defaultdict(int)
        res = []
    
        for word in words:
            # Use a set to avoid counting duplicates within the same word
            unique_chars = set(word)
            for char in unique_chars:
                m[char] += 1
        
        # Collect characters that appear in every word
        for char in m:
            if m[char] == n:
                # Find the minimum count of the character across all words
                min_count = min(word.count(char) for word in words)
                res.extend([char] * min_count)
        
        return res
        