class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        mp = defaultdict(int)

        for a, b in paths:
            mp[a] += 1
            mp[b] -= 1
        
        for a, b in mp.items():
            if b == -1:
                return a
        
        