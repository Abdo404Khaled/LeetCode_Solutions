class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, workers):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))
        workers.sort()
        
        i, mx, res, n = 0, 0, 0, len(workers)

        for worker in workers:

            while i < n and jobs[i][0] <= worker:
                mx = max(mx, jobs[i][1])
                i += 1
            
            res += mx
        
        return res




        
        

        