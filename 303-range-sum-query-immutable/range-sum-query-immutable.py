class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = []
        sum = 0
        for n in nums:
            sum += n
            self.prefix.append(sum)        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if(left == 0):
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)