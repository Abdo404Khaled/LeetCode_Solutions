class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        stand, flag = 1, 1

        while time:
            time -= 1
            if flag:
                stand += 1
                if stand == n:
                    flag = not flag
            else:
                stand -= 1
                if stand == 1:
                    flag = not flag
                    
        return stand