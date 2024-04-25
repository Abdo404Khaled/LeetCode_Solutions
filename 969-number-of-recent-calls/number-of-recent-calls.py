class RecentCounter(object):

    def __init__(self):
        self.counter = deque()
        self.k = 3000

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.counter.append(t)

        while self.counter[0] < t - self.k:
            self.counter.popleft()
        
        return len(self.counter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)