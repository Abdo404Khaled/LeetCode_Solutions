class Solution:
    def minOperations(self, nums,k):
        xor = 0
        flips = 0
        for num in nums:
            xor ^= num

        xor ^= k

        if not xor:
            return 0
        else:
            for i in range(32):
                flips += (xor >> i) & 1
        return flips