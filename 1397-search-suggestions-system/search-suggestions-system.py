class TrieNode:
    def __init__(self):
        self.children = {}
        self.products = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.products.append(word)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return sorted(node.products)[:3]
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for product in products:
            trie.insert(product)

        prefix = ""
        result = []
        for char in searchWord:
            prefix += char
            result.append(trie.search(prefix))

        return result

        