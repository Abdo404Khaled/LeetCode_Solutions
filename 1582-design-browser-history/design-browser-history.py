class Node():
    def __init__(self, page = ''):
        self.page = page
        self.next = None
        self.prev = None


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.root = Node(homepage)
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        newPage = Node(url)

        self.root.next = newPage
        newPage.prev = self.root

        self.root = newPage

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        i = 0
        while self.root and self.root.prev and i < steps:
            self.root = self.root.prev
            i += 1
        return self.root.page

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        i = 0
        while self.root and self.root.next and i < steps:
            self.root = self.root.next
            i += 1
        return self.root.page
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)