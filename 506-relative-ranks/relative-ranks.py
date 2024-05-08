class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        scores = [(s, i) for i, s in enumerate(score)]
        scores.sort()
        res = []
        for i in range(len(scores)):
            s, index = scores.pop()
            if i == 0:
                score[index] = "Gold Medal"
            elif i == 1:
                score[index] = "Silver Medal"
            elif i == 2:
                score[index] = "Bronze Medal"
            else:
                score[index] = str(i + 1)
        
        return score
        
            

