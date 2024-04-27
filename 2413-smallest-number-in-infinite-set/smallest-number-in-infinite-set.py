class SmallestInfiniteSet:

    def __init__(self):
        self.present = [True for _ in range(1, 1001)]
        self.heap = [i for i in range(1, 1001)]
        
    def popSmallest(self):
        number = heapq.heappop(self.heap)
        self.present[number - 1] = False
        return number
        
    def addBack(self, num):
        if not self.present[num - 1]:
            heapq.heappush(self.heap, num)
            self.present[num - 1] = True
        else:
            pass