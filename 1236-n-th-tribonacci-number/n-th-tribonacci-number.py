class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = [0, 1, 1]

        if n in [0, 1, 2]:
            return mem[n]
        
        for i in range(3, n + 1):
            mem.append(mem[i - 1] + mem[i - 2] + mem[i - 3])
        
        return mem[n]