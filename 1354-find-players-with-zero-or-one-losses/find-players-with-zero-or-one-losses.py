class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        losers = defaultdict(int)
        players = set()

        for winner, loser in matches:
            losers[loser] += 1
            players.add(winner)
            players.add(loser)
        
        zeros, ones = [], []

        for player in players:
            if player not in losers:
                zeros.append(player)
            elif losers[player] == 1:
                ones.append(player)
        
        return [sorted(zeros), sorted(ones)]

        