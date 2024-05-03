class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        parts1, parts2 = version1.split("."), version2.split(".")
        n, m = len(parts1), len(parts2)
        i, j = n - 1, m - 1
        while parts1 != [] and int(parts1[i]) == 0:
            parts1.pop()
            i -= 1
        while parts2 != [] and int(parts2[j]) == 0:
            parts2.pop()
            j -= 1
        
        n, m = len(parts1), len(parts2)

        for x in range(min(n, m)):
            p1, p2 = int(parts1[x]), int(parts2[x])
            if p1 < p2: return -1
            elif p1 > p2: return 1

        if n > m: return 1
        elif m > n: return -1
        else: return 0
        