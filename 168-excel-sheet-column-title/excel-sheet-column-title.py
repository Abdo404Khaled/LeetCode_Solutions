class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        mapC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = ''
        while columnNumber:
            c = (columnNumber - 1) % 26
            res += mapC[c]
            columnNumber = (columnNumber - 1) // 26
        
        return res[::-1]

        