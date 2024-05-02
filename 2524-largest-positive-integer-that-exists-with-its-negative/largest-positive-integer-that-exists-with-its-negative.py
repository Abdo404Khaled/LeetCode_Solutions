class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = set()
        max_num = -float('inf')

        for num in nums:
            if -num in st:
                max_num = max(max_num, -num if num < 0 else num)
            else:
                st.add(num)

        return max_num if max_num != -float('inf') else -1