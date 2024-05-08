class StockSpanner(object):

    def __init__(self):
        self.s = [(float('inf'), -1)]
        self.span = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        i=self.span
        while self.s and self.s[-1][0] <= price:
            self.s.pop()

        ans = i - self.s[-1][1]
        self.s.append((price,i))
        self.span += 1
        return ans
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)