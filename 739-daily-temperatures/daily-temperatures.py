class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures) 
        res = [0] * n
        s = []

        for i in range(n - 1, -1, -1):
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            
            res[i] = 0 if not s else s[-1] - i
            s.append(i)
        
        return res
        