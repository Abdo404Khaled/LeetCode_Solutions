class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        n = len(derived)
        dp = {}

        def dfs(i, first, prev):
            if i == n:
                return (prev ^ first) == derived[-1]
            if (i, first, prev) in dp:
                return dp[(i, first, prev)]
            current = False
            if i == 0 or (prev ^ 0) == derived[i - 1]:
                current |= dfs(i + 1, first if i > 0 else 0, 0)
            if i == 0 or (prev ^ 1) == derived[i - 1]:
                current |= dfs(i + 1, first if i > 0 else 1, 1)
            dp[(i, first, prev)] = current
            return current

        return dfs(0, 0, 0) or dfs(0, 1, 1)

                


        