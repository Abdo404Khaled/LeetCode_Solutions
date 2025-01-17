class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        n = len(derived)
        xor_sum = 0

        for num in derived:
            xor_sum ^= num
        
        return xor_sum == 0
                


        