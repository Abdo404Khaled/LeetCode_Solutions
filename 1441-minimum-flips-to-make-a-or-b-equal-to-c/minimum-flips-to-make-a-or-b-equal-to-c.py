class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            a_bit = a >> i & 1
            b_bit = b >> i & 1
            c_bit = c >> i & 1
            if not c_bit:
                res += a_bit + b_bit
            elif c_bit and (not a_bit and not b_bit):
                res += 1
        return res