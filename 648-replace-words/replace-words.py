class Trie():
    def __init__(self, val=''):
        self.val = val
        self.children = {}
        self.isEnd = False

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for word in dictionary:
            curr = trie
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = Trie(curr.val + letter)
                curr = curr.children[letter]
            curr.isEnd = True
        
        res = ""
        for word in sentence.split():
            curr = trie
            for letter in word:
                if letter in curr.children:
                    curr = curr.children[letter]
                    if curr.isEnd:
                        res += curr.val + " "
                        break
                else:
                    res += word + " "
                    break
            else:
                res += word + " "
        
        return res.strip()