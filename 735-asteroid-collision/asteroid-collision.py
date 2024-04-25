class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        q = []
        
        for ast in asteroids:
            while q and ast < 0 and q[-1] > 0:
                diff = ast + q[-1]
                if not diff:
                    ast = 0
                    q.pop()
                elif diff >= 0:
                    ast = 0
                else:
                    q.pop()
            if ast:
                q.append(ast)

        return q