class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        res = 0
        if len(s) == 1:
            return num

        for c in s:
            res += int(c)
        return self.addDigits(res)

        