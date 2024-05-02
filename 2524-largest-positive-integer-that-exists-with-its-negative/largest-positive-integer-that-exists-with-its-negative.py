class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = set()
        for num in nums:
            st.add(num)
        max_num = -1001
        for num in nums:
            if num >0:
                if -1*num in st:
                    max_num = max(max_num,num)
        if max_num ==-1001:return -1
        else:return max_num