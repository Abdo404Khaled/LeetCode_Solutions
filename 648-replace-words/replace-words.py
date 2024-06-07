class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        for letter in dictionary:
            for i, word in enumerate(words):
                if word.startswith(letter):
                    words[i] = letter
        
        return " ".join(words)
        